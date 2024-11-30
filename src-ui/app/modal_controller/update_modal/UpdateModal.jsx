import styles from "./UpdateModal.module.scss";
import { useTranslation } from "react-i18next";
import { useStore_OpenedQuickSetting } from "@store";
import { useUpdateSoftware } from "@logics_common";

export const UpdateModal = () => {
    const { t } = useTranslation();
    const { updateOpenedQuickSetting } = useStore_OpenedQuickSetting();
    const { updateSoftware } = useUpdateSoftware();

    return (
        <div className={styles.container}>
            <p className={styles.label}>{t("main_page.confirmation_message.update_software")}</p>
            <div className={styles.button_wrapper}>
                <button className={styles.deny_button} onClick={() => updateOpenedQuickSetting("")} >{t("main_page.confirmation_message.deny_update_software")}</button>
                <button className={styles.accept_button} onClick={() => updateSoftware()}>{t("main_page.confirmation_message.accept_update_software")}</button>
            </div>
        </div>
    );
};