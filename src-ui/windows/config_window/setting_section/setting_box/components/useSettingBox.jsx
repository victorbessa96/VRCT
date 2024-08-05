import styles from "./useSettingBox.module.scss";
import { useIsOpenedDropdownMenu } from "@store";
import clsx from "clsx";

import { LabelComponent } from "./label_component/LabelComponent";
import { DropdownMenu } from "./dropdown_menu/DropdownMenu";
import { Slider } from "./slider/Slider";
import { Checkbox } from "./checkbox/Checkbox";
import { Switchbox } from "./switchbox/Switchbox";
import { Entry } from "./entry/Entry";
import { ThresholdComponent } from "./threshold_component/ThresholdComponent";
import { RadioButton } from "./radio_button/RadioButton";
import { OpenWebpage_DeeplAuthKey, DeeplAuthKey } from "./deepl_auth_key/DeeplAuthKey";
import { MessageFormat } from "./message_format/MessageFormat";

export const useSettingBox = () => {
    const { updateIsOpenedDropdownMenu } = useIsOpenedDropdownMenu();

    const DropdownMenuContainer = (props) => {
        const onMouseLeaveFunction = () => {
            updateIsOpenedDropdownMenu("");
        };

        return (
            <div className={styles.container} onMouseLeave={onMouseLeaveFunction}>
                <LabelComponent label={props.label} desc={props.desc} />
                <DropdownMenu {...props}/>
            </div>
        );
    };

    const SliderContainer = (props) => {
        return (
            <div className={styles.container}>
                <LabelComponent label={props.label} desc={props.desc} />
                <Slider {...props}/>
            </div>
        );
    };

    const CheckboxContainer = (props) => {
        return (
            <div className={styles.container}>
                <LabelComponent label={props.label} desc={props.desc} />
                <Checkbox {...props}/>
            </div>
        );
    };

    const SwitchboxContainer = (props) => {
        return (
            <div className={styles.container}>
                <LabelComponent label={props.label} desc={props.desc} />
                <Switchbox {...props}/>
            </div>
        );
    };

    const EntryContainer = (props) => {
        return (
            <div className={styles.container}>
                <LabelComponent label={props.label} desc={props.desc} />
                <Entry {...props}/>
            </div>
        );
    };

    const RadioButtonContainer = (props) => {
        return (
            <div className={styles.container}>
                <LabelComponent label={props.label} desc={props.desc} />
                <RadioButton {...props}/>
            </div>
        );
    };

    const ThresholdContainer = (props) => {
        return (
            <div className={styles.threshold_container}>
                <div className={styles.threshold_switch_section}>
                    <LabelComponent label={props.label} desc={props.desc} />
                    <Switchbox {...props}/>
                </div>
                <div className={styles.threshold_section}>
                    <ThresholdComponent {...props}/>
                </div>
            </div>
        );
    };

    const DeeplAuthKeyContainer = (props) => {
        return (
            <div className={styles.container}>
                <div className={styles.deepl_auth_key_label_section}>
                    <LabelComponent label={props.label} desc={props.desc} />
                    <OpenWebpage_DeeplAuthKey />
                </div>
                <DeeplAuthKey {...props}/>
            </div>
        );
    };


    const MessageFormatContainer = (props) => {
        return (
            <div className={clsx(styles.container, styles.flex_column)}>
                <div className={styles.label_only_section}>
                    <LabelComponent label={props.label} desc={props.desc} />
                </div>
                <div className={styles.message_format_section}>
                    <MessageFormat {...props}/>
                </div>
            </div>
        );
    };

    return {
        DropdownMenuContainer,
        SliderContainer,
        CheckboxContainer,
        SwitchboxContainer,
        EntryContainer,
        ThresholdContainer,
        RadioButtonContainer,
        DeeplAuthKeyContainer,
        MessageFormatContainer,
    };
};