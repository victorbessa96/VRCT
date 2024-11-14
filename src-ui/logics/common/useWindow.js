import { useStdoutToPython } from "@logics/useStdoutToPython";
import { useEffect } from "react";
import { appWindow, currentMonitor, availableMonitors, LogicalPosition, LogicalSize } from "@tauri-apps/api/window";
export const useWindow = () => {
    const { asyncStdoutToPython } = useStdoutToPython();
    const asyncGetWindowGeometry = async () => {
        try {
            const position = await appWindow.outerPosition();
            const { x, y } = position;

            const size = await appWindow.outerSize();
            const { width, height } = size;

            return {
                x_pos: x,
                y_pos: y,
                width: width,
                height: height
            };
        } catch (err) {
            console.error("Error getting window position and size:", err);
        }
    };

    const asyncSaveWindowGeometry = async () => {
        const minimized = await appWindow.isMinimized();
        if (minimized === true) return; // don't save while the window is minimized.
        const data = await asyncGetWindowGeometry();
        asyncStdoutToPython("/set/data/main_window_geometry", data);
    };

    const restoreWindowGeometry = async (data) => {
        try {
            const monitors = await availableMonitors();
            const { x_pos, y_pos, width, height } = data;

            // ウィンドウが属するモニターを特定
            const targetMonitor = monitors.find(monitor =>
                x_pos >= monitor.position.x &&
                y_pos >= monitor.position.y &&
                x_pos < monitor.position.x + monitor.size.width &&
                y_pos < monitor.position.y + monitor.size.height
            ) || await currentMonitor();

            if (targetMonitor) {
                const { width: monitorWidth, height: monitorHeight } = targetMonitor.size;
                const { x: monitorX, y: monitorY } = targetMonitor.position;

                // ウィンドウのサイズをモニターサイズ内に収める
                let adjustedWidth = Math.min(parseInt(width), monitorWidth);
                let adjustedHeight = Math.min(parseInt(height), monitorHeight);

                // ウィンドウの位置をモニターの範囲内に収める
                let adjustedX = parseInt(x_pos);
                let adjustedY = parseInt(y_pos);

                // X座標がモニター左にはみ出ている場合
                if (adjustedX < monitorX) {
                    adjustedX = monitorX;
                }
                // X座標がモニター右にはみ出ている場合
                else if (adjustedX + adjustedWidth > monitorX + monitorWidth) {
                    adjustedX = monitorX + monitorWidth - adjustedWidth;
                }

                // Y座標がモニター上にはみ出ている場合
                if (adjustedY < monitorY) {
                    adjustedY = monitorY;
                }
                // Y座標がモニター下にはみ出ている場合
                else if (adjustedY + adjustedHeight > monitorY + monitorHeight) {
                    adjustedY = monitorY + monitorHeight - adjustedHeight;
                }

                await appWindow.setPosition(new LogicalPosition(adjustedX, adjustedY));
                await appWindow.setSize(new LogicalSize(adjustedWidth, adjustedHeight));
            } else {
                console.error("Monitor information could not be retrieved.");
            }
        } catch (err) {
            console.error("Error setting window position and size:", err);
        }
    };


    const WindowGeometryController = () => {
        useEffect(() => {
            let resizeTimeout;
            const unlistenResize = appWindow.onResized(() => {
                clearTimeout(resizeTimeout);
                resizeTimeout = setTimeout(asyncSaveWindowGeometry, 200);
            });

            return () => {
                unlistenResize.then((dispose) => dispose());
            };
        }, []);

        useEffect(() => {
            let moveTimeout;
            const unlistenMove = appWindow.onMoved(() => {
                clearTimeout(moveTimeout);
                moveTimeout = setTimeout(asyncSaveWindowGeometry, 200);
            });

            return () => {
                unlistenMove.then((dispose) => dispose());
            };
        }, []);

        return null;
    };

    return {
        WindowGeometryController,
        asyncSaveWindowGeometry,
        restoreWindowGeometry,
    };
};