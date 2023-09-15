from typing import Union
from types import SimpleNamespace
from tkinter import font as tk_font
from languages import selectable_languages

from customtkinter import StringVar, IntVar, BooleanVar, END as CTK_END, get_appearance_mode
from vrct_gui.ui_managers import ColorThemeManager, ImageFileManager, UiScalingManager
from vrct_gui import vrct_gui

from config import config

class View():
    def __init__(self):
        self.settings = SimpleNamespace()
        theme = get_appearance_mode() if config.APPEARANCE_THEME == "System" else config.APPEARANCE_THEME
        all_ctm = ColorThemeManager(theme)
        all_uism = UiScalingManager(config.UI_SCALING)
        image_file = ImageFileManager(theme)

        common_args = {
            "image_file": image_file,
            "FONT_FAMILY": config.FONT_FAMILY,
        }

        self.settings.main = SimpleNamespace(
            ctm=all_ctm.main,
            uism=all_uism.main,
            COMPACT_MODE_ICON_SIZE=0,
            **common_args
        )

        self.settings.config_window = SimpleNamespace(
            ctm=all_ctm.config_window,
            uism=all_uism.config_window,
            IS_CONFIG_WINDOW_COMPACT_MODE=config.IS_CONFIG_WINDOW_COMPACT_MODE,
            **common_args
        )

        self.settings.selectable_language_window = SimpleNamespace(
            ctm=all_ctm.selectable_language_window,
            uism=all_uism.config_window,
            **common_args
        )

        self.view_variable = SimpleNamespace(
            # Open Config Window
            CALLBACK_OPEN_CONFIG_WINDOW=None,
            CALLBACK_CLOSE_CONFIG_WINDOW=None,


            # Main Window
            # Sidebar
            # Sidebar Compact Mode
            IS_MAIN_WINDOW_SIDEBAR_COMPACT_MODE=False,
            CALLBACK_TOGGLE_MAIN_WINDOW_SIDEBAR_COMPACT_MODE=None,

            # Sidebar Features
            VAR_LABEL_TRANSLATION=StringVar(value="Translation"),
            CALLBACK_TOGGLE_TRANSLATION=None,

            VAR_LABEL_TRANSCRIPTION_SEND=StringVar(value="Voice2Chatbox"),
            CALLBACK_TOGGLE_TRANSCRIPTION_SEND=None,

            VAR_LABEL_TRANSCRIPTION_RECEIVE=StringVar(value="Speaker2Log"),
            CALLBACK_TOGGLE_TRANSCRIPTION_RECEIVE=None,

            VAR_LABEL_FOREGROUND=StringVar(value="Foreground"),
            CALLBACK_TOGGLE_FOREGROUND=None,

            # Sidebar Language Settings
            VAR_LABEL_LANGUAGE_SETTINGS=StringVar(value="Language Settings"), # JA: 言語設定
            LIST_SELECTABLE_LANGUAGES=[],
            CALLBACK_SELECTED_LANGUAGE_PRESET_TAB=None,

            VAR_LABEL_YOUR_LANGUAGE=StringVar(value="Your Language"), # JA: あなたの言語
            VAR_YOUR_LANGUAGE = StringVar(value="Japanese\n(Japan)"),
            CALLBACK_OPEN_SELECTABLE_YOUR_LANGUAGE_WINDOW=None,
            IS_OPENED_SELECTABLE_YOUR_LANGUAGE_WINDOW=False,
            CALLBACK_SELECTED_YOUR_LANGUAGE=None,

            VAR_LABEL_BOTH_DIRECTION_DESC=StringVar(value="Translate Each Other"), # JA: 双方向に翻訳

            VAR_LABEL_TARGET_LANGUAGE=StringVar(value="Target Language"), # JA: 相手の言語
            VAR_TARGET_LANGUAGE = StringVar(value="English\n(United States)"),
            CALLBACK_OPEN_SELECTABLE_TARGET_LANGUAGE_WINDOW=None,
            IS_OPENED_SELECTABLE_TARGET_LANGUAGE_WINDOW=False,
            CALLBACK_SELECTED_TARGET_LANGUAGE=None,


            VAR_LABEL_TEXTBOX_ALL=StringVar(value="All"), # JA: 全て
            VAR_LABEL_TEXTBOX_SENT=StringVar(value="Sent"), # JA: 送信
            VAR_LABEL_TEXTBOX_RECEIVED=StringVar(value="Received"), # JA: 受信
            VAR_LABEL_TEXTBOX_SYSTEM=StringVar(value="System"), # JA: システム


            # Selectable Language Window
            VAR_TITLE_LABEL_SELECTABLE_LANGUAGE=StringVar(value=""),
            VAR_GO_BACK_LABEL_SELECTABLE_LANGUAGE=StringVar(value="Go Back"),



            # Config Window
            # Appearance Tab
            VAR_LABEL_TRANSPARENCY=StringVar(value="Transparency"),
            VAR_DESC_TRANSPARENCY=StringVar(value="Change the window's transparency. 50% to 100%. (Default: 100%)"),
            SLIDER_RANGE_TRANSPARENCY=(50, 100),
            CALLBACK_SET_TRANSPARENCY=None,
            VAR_TRANSPARENCY=IntVar(value=config.TRANSPARENCY),

            VAR_LABEL_APPEARANCE_THEME=StringVar(value="Theme"),
            VAR_DESC_APPEARANCE_THEME=StringVar(value="Change the color theme from \"Light\" and \"Dark\". If you select \"System\", It will adjust based on your Windows theme. (Default: System)"),
            LIST_APPEARANCE_THEME=["Light", "Dark", "System"],
            CALLBACK_SET_APPEARANCE_THEME=None,
            VAR_APPEARANCE_THEME=StringVar(value=config.APPEARANCE_THEME),

            VAR_LABEL_UI_SCALING=StringVar(value="UI Size"),
            VAR_DESC_UI_SCALING=StringVar(value="(Default: 100%)"),
            LIST_UI_SCALING=["80%", "90%", "100%", "110%", "120%"],
            CALLBACK_SET_UI_SCALING=None,
            VAR_UI_SCALING=StringVar(value=config.UI_SCALING),

            VAR_LABEL_FONT_FAMILY=StringVar(value="Font Family"),
            VAR_DESC_FONT_FAMILY=StringVar(value="(Default: Yu Gothic UI)"),
            LIST_FONT_FAMILY=list(tk_font.families()),
            CALLBACK_SET_FONT_FAMILY=None,
            VAR_FONT_FAMILY=StringVar(value=config.FONT_FAMILY),

            VAR_LABEL_UI_LANGUAGE=StringVar(value="UI Language"),
            VAR_DESC_UI_LANGUAGE=StringVar(value="(Default: English)"),
            LIST_UI_LANGUAGE=list(selectable_languages.values()),
            CALLBACK_SET_UI_LANGUAGE=None,
            VAR_UI_LANGUAGE=StringVar(value=selectable_languages[config.UI_LANGUAGE]),


            # Translation Tab
            VAR_LABEL_DEEPL_AUTH_KEY=StringVar(value="DeepL Auth Key"),
            VAR_DESC_DEEPL_AUTH_KEY=None,
            # VAR_DESC_DEEPL_AUTH_KEY=StringVar(value=""),
            CALLBACK_SET_DEEPL_AUTH_KEY=None,
            VAR_DEEPL_AUTH_KEY=StringVar(value=config.AUTH_KEYS["DeepL(auth)"]),


            # Transcription Tab (Mic)
            VAR_LABEL_MIC_HOST=StringVar(value="Mic Host"),
            VAR_DESC_MIC_HOST=StringVar(value="Select the mic host. (Default: ?)"),
            LIST_MIC_HOST=[],
            CALLBACK_SET_MIC_HOST=None,
            VAR_MIC_HOST=StringVar(value=config.CHOICE_MIC_HOST),

            VAR_LABEL_MIC_DEVICE=StringVar(value="Mic Device"),
            VAR_DESC_MIC_DEVICE=StringVar(value="Select the mic devise. (Default: ?)"),
            LIST_MIC_DEVICE=[],
            CALLBACK_SET_MIC_DEVICE=None,
            VAR_MIC_DEVICE=StringVar(value=config.CHOICE_MIC_DEVICE),

            VAR_LABEL_MIC_ENERGY_THRESHOLD=StringVar(value="Mic Energy Threshold"),
            VAR_DESC_MIC_ENERGY_THRESHOLD=StringVar(value="Slider to modify the threshold for activating voice input.\nPress the microphone button to start input and speak something, so you can adjust it while monitoring the actual volume. 0 to 2000 (Default: 300)"),
            SLIDER_RANGE_MIC_ENERGY_THRESHOLD=(0, config.MAX_MIC_ENERGY_THRESHOLD),
            CALLBACK_CHECK_MIC_THRESHOLD=None,
            VAR_MIC_ENERGY_THRESHOLD__SLIDER=IntVar(value=config.INPUT_MIC_ENERGY_THRESHOLD),
            VAR_MIC_ENERGY_THRESHOLD__ENTRY=StringVar(value=config.INPUT_MIC_ENERGY_THRESHOLD),

            VAR_LABEL_MIC_DYNAMIC_ENERGY_THRESHOLD=StringVar(value="Mic Dynamic Energy Threshold"),
            VAR_DESC_MIC_DYNAMIC_ENERGY_THRESHOLD=StringVar(value="When this feature is selected, it will automatically adjust in a way that works well, based on the set Mic Energy Threshold."),
            CALLBACK_SET_MIC_DYNAMIC_ENERGY_THRESHOLD=None,
            VAR_MIC_DYNAMIC_ENERGY_THRESHOLD=BooleanVar(value=config.INPUT_MIC_DYNAMIC_ENERGY_THRESHOLD),

            VAR_LABEL_MIC_RECORD_TIMEOUT=StringVar(value="Mic Record Timeout"),
            VAR_DESC_MIC_RECORD_TIMEOUT=StringVar(value="(Default: 3)"),
            CALLBACK_SET_MIC_RECORD_TIMEOUT=None,
            VAR_MIC_RECORD_TIMEOUT=StringVar(value=config.INPUT_MIC_RECORD_TIMEOUT),

            VAR_LABEL_MIC_PHRASE_TIMEOUT=StringVar(value="Mic Phrase Timeout"),
            VAR_DESC_MIC_PHRASE_TIMEOUT=StringVar(value="(Default: 3)"),
            CALLBACK_SET_MIC_PHRASE_TIMEOUT=None,
            VAR_MIC_PHRASE_TIMEOUT=StringVar(value=config.INPUT_MIC_PHRASE_TIMEOUT),

            VAR_LABEL_MIC_MAX_PHRASES=StringVar(value="Mic Max Phrases"),
            VAR_DESC_MIC_MAX_PHRASES=StringVar(value="It will stop recording and send the recordings when the set count of phrase(s) is reached. (Default: 10)"),
            CALLBACK_SET_MIC_MAX_PHRASES=None,
            VAR_MIC_MAX_PHRASES=StringVar(value=config.INPUT_MIC_MAX_PHRASES),

            VAR_LABEL_MIC_WORD_FILTER=StringVar(value="Mic Word Filter"),
            VAR_DESC_MIC_WORD_FILTER=StringVar(value="It will not send the sentence if the word(s) included in the set list of words.\nHow to set: e.g. AAA,BBB,CCC"),
            CALLBACK_SET_MIC_WORD_FILTER=None,
            VAR_MIC_WORD_FILTER=StringVar(value=",".join(config.INPUT_MIC_WORD_FILTER) if len(config.INPUT_MIC_WORD_FILTER) > 0 else ""),


            # Transcription Tab (Speaker)
            VAR_LABEL_SPEAKER_DEVICE=StringVar(value="Speaker Device"),
            VAR_DESC_SPEAKER_DEVICE=StringVar(value="Select the speaker devise. (Default: ?)"),
            LIST_SPEAKER_DEVICE=[],
            CALLBACK_SET_SPEAKER_DEVICE=None,
            VAR_SPEAKER_DEVICE=StringVar(value=config.CHOICE_SPEAKER_DEVICE),

            VAR_LABEL_SPEAKER_ENERGY_THRESHOLD=StringVar(value="Mic Energy Threshold"),
            VAR_DESC_SPEAKER_ENERGY_THRESHOLD=StringVar(value="Slider to modify the threshold for activating voice input.\nPress the headphones mark button to start input and speak something, so you can adjust it while monitoring the actual volume. 0 to 4000 (Default: 300)"),
            SLIDER_RANGE_SPEAKER_ENERGY_THRESHOLD=(0, config.MAX_SPEAKER_ENERGY_THRESHOLD),
            CALLBACK_CHECK_SPEAKER_THRESHOLD=None,
            VAR_SPEAKER_ENERGY_THRESHOLD__SLIDER=IntVar(value=config.INPUT_SPEAKER_ENERGY_THRESHOLD),
            VAR_SPEAKER_ENERGY_THRESHOLD__ENTRY=StringVar(value=config.INPUT_SPEAKER_ENERGY_THRESHOLD),

            VAR_LABEL_SPEAKER_DYNAMIC_ENERGY_THRESHOLD=StringVar(value="Speaker Dynamic Energy Threshold"),
            VAR_DESC_SPEAKER_DYNAMIC_ENERGY_THRESHOLD=StringVar(value="When this feature is selected, it will automatically adjust in a way that works well, based on the set Speaker Energy Threshold."),
            CALLBACK_SET_SPEAKER_DYNAMIC_ENERGY_THRESHOLD=None,
            VAR_SPEAKER_DYNAMIC_ENERGY_THRESHOLD=BooleanVar(value=config.INPUT_SPEAKER_DYNAMIC_ENERGY_THRESHOLD),

            VAR_LABEL_SPEAKER_RECORD_TIMEOUT=StringVar(value="Speaker Record Timeout"),
            VAR_DESC_SPEAKER_RECORD_TIMEOUT=StringVar(value="(Default: 3)"),
            CALLBACK_SET_SPEAKER_RECORD_TIMEOUT=None,
            VAR_SPEAKER_RECORD_TIMEOUT=StringVar(value=config.INPUT_SPEAKER_RECORD_TIMEOUT),

            VAR_LABEL_SPEAKER_PHRASE_TIMEOUT=StringVar(value="Speaker Phrase Timeout"),
            VAR_DESC_SPEAKER_PHRASE_TIMEOUT=StringVar(value="It will stop recording and receive the recordings when the set second(s) is reached. (Default: 3)"),
            CALLBACK_SET_SPEAKER_PHRASE_TIMEOUT=None,
            VAR_SPEAKER_PHRASE_TIMEOUT=StringVar(value=config.INPUT_SPEAKER_PHRASE_TIMEOUT),

            VAR_LABEL_SPEAKER_MAX_PHRASES=StringVar(value="Speaker Max Phrases"),
            VAR_DESC_SPEAKER_MAX_PHRASES=StringVar(value="It will stop recording and receive the recordings when the set count of phrase(s) is reached. (Default: 10)"),
            CALLBACK_SET_SPEAKER_MAX_PHRASES=None,
            VAR_SPEAKER_MAX_PHRASES=StringVar(value=config.INPUT_SPEAKER_MAX_PHRASES),


            # Others Tab
            VAR_LABEL_ENABLE_AUTO_CLEAR_MESSAGE_BOX=StringVar(value="Auto Clear The Message Box"),
            VAR_DESC_ENABLE_AUTO_CLEAR_MESSAGE_BOX=StringVar(value="Clear the message box after sending your message."),
            CALLBACK_SET_ENABLE_AUTO_CLEAR_MESSAGE_BOX=None,
            VAR_ENABLE_AUTO_CLEAR_MESSAGE_BOX=BooleanVar(value=config.ENABLE_AUTO_CLEAR_MESSAGE_BOX),

            VAR_LABEL_ENABLE_NOTICE_XSOVERLAY=StringVar(value="Notification XSOverlay (VR Only)"),
            VAR_DESC_ENABLE_NOTICE_XSOVERLAY=StringVar(value="Notify received messages by using XSOverlay's notification feature."),
            CALLBACK_SET_ENABLE_NOTICE_XSOVERLAY=None,
            VAR_ENABLE_NOTICE_XSOVERLAY=BooleanVar(value=config.ENABLE_NOTICE_XSOVERLAY),

            VAR_LABEL_ENABLE_AUTO_EXPORT_MESSAGE_LOGS=StringVar(value="Auto Export Message Logs"),
            VAR_DESC_ENABLE_AUTO_EXPORT_MESSAGE_LOGS=StringVar(value="Automatically export the conversation messages as a text file."),
            CALLBACK_SET_ENABLE_AUTO_EXPORT_MESSAGE_LOGS=None,
            VAR_ENABLE_AUTO_EXPORT_MESSAGE_LOGS=BooleanVar(value=config.ENABLE_LOGGER),


            VAR_LABEL_MESSAGE_FORMAT=StringVar(value="Message Format"),
            VAR_DESC_MESSAGE_FORMAT=StringVar(value="You can change the decoration of the message you want to send. (Default: \"[message]([translation])\" )"),
            CALLBACK_SET_MESSAGE_FORMAT=None,
            VAR_MESSAGE_FORMAT=StringVar(value=config.MESSAGE_FORMAT),


            # Advanced Settings Tab
            VAR_LABEL_OSC_IP_ADDRESS=StringVar(value="OSC IP Address"),
            VAR_DESC_OSC_IP_ADDRESS=StringVar(value="(Default: 127.0.0.1)"),
            CALLBACK_SET_OSC_IP_ADDRESS=None,
            VAR_OSC_IP_ADDRESS=StringVar(value=config.OSC_IP_ADDRESS),

            VAR_LABEL_OSC_PORT=StringVar(value="OSC Port"),
            VAR_DESC_OSC_PORT=StringVar(value="(Default: 9000)"),
            CALLBACK_SET_OSC_PORT=None,
            VAR_OSC_PORT=StringVar(value=config.OSC_PORT),
        )



    def register(
            self,
            window_action_registers=None,
            sidebar_features_registers=None,
            language_presets_registers=None,
            entry_message_box_registers=None,
            config_window_registers=None
        ):


        # Open Config Window
        if window_action_registers is not None:
            self.view_variable.CALLBACK_OPEN_CONFIG_WINDOW=window_action_registers.get("callback_open_config_window", None)
            self.view_variable.CALLBACK_CLOSE_CONFIG_WINDOW=window_action_registers.get("callback_close_config_window", None)



        self.view_variable.CALLBACK_TOGGLE_MAIN_WINDOW_SIDEBAR_COMPACT_MODE = self._toggleMainWindowSidebarCompactMode

        if sidebar_features_registers is not None:
            self.view_variable.CALLBACK_TOGGLE_TRANSLATION = sidebar_features_registers.get("callback_toggle_translation", None)
            self.view_variable.CALLBACK_TOGGLE_TRANSCRIPTION_SEND = sidebar_features_registers.get("callback_toggle_transcription_send", None)
            self.view_variable.CALLBACK_TOGGLE_TRANSCRIPTION_RECEIVE = sidebar_features_registers.get("callback_toggle_transcription_receive", None)
            self.view_variable.CALLBACK_TOGGLE_FOREGROUND = sidebar_features_registers.get("callback_toggle_foreground", None)

        if language_presets_registers is not None:
            self.view_variable.CALLBACK_SELECTED_YOUR_LANGUAGE = language_presets_registers.get("callback_your_language", None)
            self.view_variable.CALLBACK_SELECTED_TARGET_LANGUAGE = language_presets_registers.get("callback_target_language", None)
            language_presets_registers.get("values", None) and self.updateList_selectableLanguages(language_presets_registers["values"])

            self.view_variable.CALLBACK_SELECTED_LANGUAGE_PRESET_TAB = language_presets_registers.get("callback_selected_language_preset_tab", None)

        self.updateGuiVariableByPresetTabNo(config.SELECTED_TAB_NO)
        vrct_gui.setDefaultActiveLanguagePresetTab(tab_no=config.SELECTED_TAB_NO)



        self.view_variable.CALLBACK_OPEN_SELECTABLE_YOUR_LANGUAGE_WINDOW = self.openSelectableLanguagesWindow_YourLanguage
        self.view_variable.CALLBACK_OPEN_SELECTABLE_TARGET_LANGUAGE_WINDOW = self.openSelectableLanguagesWindow_TargetLanguage

        entry_message_box = getattr(vrct_gui, "entry_message_box")
        if entry_message_box_registers is not None:
            entry_message_box.bind("<Return>", entry_message_box_registers.get("bind_Return"))
            entry_message_box.bind("<Any-KeyPress>", entry_message_box_registers.get("bind_Any_KeyPress"))


        entry_message_box.bind("<FocusIn>", self._foregroundOffForcefully)
        entry_message_box.bind("<FocusOut>", self._foregroundOnForcefully)


        # Config Window
        # Compact Mode Switch
        if config_window_registers is not None:

            self.view_variable.CALLBACK_ENABLE_CONFIG_WINDOW_COMPACT_MODE = config_window_registers.get("callback_disable_config_window_compact_mode", None)
            self.view_variable.CALLBACK_DISABLE_CONFIG_WINDOW_COMPACT_MODE = config_window_registers.get("callback_enable_config_window_compact_mode", None)


            # Appearance Tab
            self.view_variable.CALLBACK_SET_TRANSPARENCY = config_window_registers.get("callback_set_transparency", None)

            self.view_variable.CALLBACK_SET_APPEARANCE = config_window_registers.get("callback_set_appearance", None)
            self.view_variable.CALLBACK_SET_UI_SCALING = config_window_registers.get("callback_set_ui_scaling", None)
            self.view_variable.CALLBACK_SET_FONT_FAMILY = config_window_registers.get("callback_set_font_family", None)
            self.view_variable.CALLBACK_SET_UI_LANGUAGE = config_window_registers.get("callback_set_ui_language", None)


            # Translation Tab
            self.view_variable.CALLBACK_SET_DEEPL_AUTHKEY = config_window_registers.get("callback_set_deepl_authkey", None)

            # Transcription Tab (Mic)
            self.view_variable.CALLBACK_SET_MIC_HOST = config_window_registers.get("callback_set_mic_host", None)
            config_window_registers.get("list_mic_host", None) and self.updateList_MicHost(config_window_registers["list_mic_host"])

            self.view_variable.CALLBACK_SET_MIC_DEVICE = config_window_registers.get("callback_set_mic_device", None)
            config_window_registers.get("list_mic_device", None) and self.updateList_MicDevice(config_window_registers["list_mic_device"])

            self.view_variable.CALLBACK_SET_MIC_ENERGY_THRESHOLD = config_window_registers.get("callback_set_mic_energy_threshold", None)
            self.view_variable.CALLBACK_SET_MIC_DYNAMIC_ENERGY_THRESHOLD = config_window_registers.get("callback_set_mic_dynamic_energy_threshold", None)
            self.view_variable.CALLBACK_CHECK_MIC_THRESHOLD = config_window_registers.get("callback_check_mic_threshold", None)
            self.view_variable.CALLBACK_SET_MIC_RECORD_TIMEOUT = config_window_registers.get("callback_set_mic_record_timeout", None)
            self.view_variable.CALLBACK_SET_MIC_PHRASE_TIMEOUT = config_window_registers.get("callback_set_mic_phrase_timeout", None)
            self.view_variable.CALLBACK_SET_MIC_MAX_PHRASES = config_window_registers.get("callback_set_mic_max_phrases", None)
            self.view_variable.CALLBACK_SET_MIC_WORD_FILTER = config_window_registers.get("callback_set_mic_word_filter", None)

            # Transcription Tab (Speaker)
            self.view_variable.CALLBACK_SET_SPEAKER_DEVICE = config_window_registers.get("callback_set_speaker_device", None)
            config_window_registers.get("list_speaker_device", None) and self.updateList_SpeakerDevice(config_window_registers["list_speaker_device"])

            self.view_variable.CALLBACK_SET_SPEAKER_ENERGY_THRESHOLD = config_window_registers.get("callback_set_speaker_energy_threshold", None)
            self.view_variable.CALLBACK_SET_SPEAKER_DYNAMIC_ENERGY_THRESHOLD = config_window_registers.get("callback_set_speaker_dynamic_energy_threshold", None)
            self.view_variable.CALLBACK_CHECK_SPEAKER_THRESHOLD = config_window_registers.get("callback_check_speaker_threshold", None)
            self.view_variable.CALLBACK_SET_SPEAKER_RECORD_TIMEOUT = config_window_registers.get("callback_set_speaker_record_timeout", None)
            self.view_variable.CALLBACK_SET_SPEAKER_PHRASE_TIMEOUT = config_window_registers.get("callback_set_speaker_phrase_timeout", None)
            self.view_variable.CALLBACK_SET_SPEAKER_MAX_PHRASES = config_window_registers.get("callback_set_speaker_max_phrases", None)

            # Others Tab
            self.view_variable.CALLBACK_SET_ENABLE_AUTO_CLEAR_MESSAGE_BOX = config_window_registers.get("callback_set_enable_auto_clear_chatbox", None)
            self.view_variable.CALLBACK_SET_ENABLE_NOTICE_XSOVERLAY = config_window_registers.get("callback_set_enable_notice_xsoverlay", None)
            self.view_variable.CALLBACK_SET_ENABLE_AUTO_EXPORT_MESSAGE_LOGS =  config_window_registers.get("callback_set_enable_auto_export_message_logs", None)
            self.view_variable.CALLBACK_SET_MESSAGE_FORMAT = config_window_registers.get("callback_set_message_format", None)

            # Advanced Settings Tab
            self.view_variable.CALLBACK_SET_OSC_IP_ADDRESS = config_window_registers.get("callback_set_osc_ip_address", None)
            self.view_variable.CALLBACK_SET_OSC_PORT = config_window_registers.get("callback_set_osc_port", None)

        # Insert sample conversation for testing.
        # self._insertSampleConversationToTextbox()



    @staticmethod
    def setMainWindowAllWidgetsStatusToNormal():
        vrct_gui.changeMainWindowWidgetsStatus("normal", "All")

    @staticmethod
    def setMainWindowAllWidgetsStatusToDisabled():
        vrct_gui.changeMainWindowWidgetsStatus("disabled", "All")



    def _foregroundOnForcefully(self, _e):
        if config.ENABLE_FOREGROUND:
            self.foregroundOn()

    def _foregroundOffForcefully(self, _e):
        if config.ENABLE_FOREGROUND:
            self.foregroundOff()


    @staticmethod
    def foregroundOn():
        vrct_gui.attributes("-topmost", True)

    @staticmethod
    def foregroundOff():
        vrct_gui.attributes("-topmost", False)


    def _toggleMainWindowSidebarCompactMode(self, is_turned_on):
        self.view_variable.IS_MAIN_WINDOW_SIDEBAR_COMPACT_MODE = is_turned_on
        vrct_gui.recreateMainWindowSidebar()

    def openSelectableLanguagesWindow_YourLanguage(self, _e):
        self.view_variable.VAR_TITLE_LABEL_SELECTABLE_LANGUAGE.set("Your Language")
        vrct_gui.openSelectableLanguagesWindow("your_language")
    def openSelectableLanguagesWindow_TargetLanguage(self, _e):
        self.view_variable.VAR_TITLE_LABEL_SELECTABLE_LANGUAGE.set("Target Language")
        vrct_gui.openSelectableLanguagesWindow("target_language")


    def updateGuiVariableByPresetTabNo(self, tab_no:str):
        self.view_variable.VAR_YOUR_LANGUAGE.set(config.SELECTED_TAB_YOUR_LANGUAGES[tab_no])
        self.view_variable.VAR_TARGET_LANGUAGE.set(config.SELECTED_TAB_TARGET_LANGUAGES[tab_no])


    def updateList_selectableLanguages(self, new_selectable_language_list:list):
        self.view_variable.LIST_SELECTABLE_LANGUAGES = new_selectable_language_list


    def printToTextbox_enableTranslation(self):
        self._printToTextbox_Info("翻訳機能をONにしました")
    def printToTextbox_disableTranslation(self):
        self._printToTextbox_Info("翻訳機能をOFFにしました")

    def printToTextbox_enableTranscriptionSend(self):
        self._printToTextbox_Info("Voice2chatbox機能をONにしました")
    def printToTextbox_disableTranscriptionSend(self):
        self._printToTextbox_Info("Voice2chatbox機能をOFFにしました")

    def printToTextbox_enableTranscriptionReceive(self):
        self._printToTextbox_Info("Speaker2chatbox機能をONにしました")
    def printToTextbox_disableTranscriptionReceive(self):
        self._printToTextbox_Info("Speaker2chatbox機能をOFFにしました")

    def printToTextbox_enableForeground(self):
        self._printToTextbox_Info("Start foreground")
    def printToTextbox_disableForeground(self):
        self._printToTextbox_Info("Stop foreground")

    def printToTextbox_AuthenticationSuccess(self):
        self._printToTextbox_Info("Auth key update completed")

    def printToTextbox_AuthenticationError(self):
        self._printToTextbox_Info("Auth Key is incorrect or Usage limit reached")

    def printToTextbox_OSCError(self):
        self._printToTextbox_Info("OSC is not enabled, please enable OSC and rejoin")

    def printToTextbox_DetectedByWordFilter(self, detected_message):
        self._printToTextbox_Info(f"Detect WordFilter :{detected_message}")


    @staticmethod
    def _printToTextbox_Info(info_message):
        vrct_gui.printToTextbox(
            target_type="SYSTEM",
            original_message=info_message,
            # translated_message="",
        )



    def printToTextbox_SentMessage(self, original_message, translated_message):
        self._printToTextbox_Sent(original_message, translated_message)

    @staticmethod
    def _printToTextbox_Sent(original_message, translated_message):
        vrct_gui.printToTextbox(
            target_type="SENT",
            original_message=original_message,
            translated_message=translated_message,
        )


    def printToTextbox_ReceivedMessage(self, original_message, translated_message):
        self._printToTextbox_Received(original_message, translated_message)

    @staticmethod
    def _printToTextbox_Received(original_message, translated_message):
        vrct_gui.printToTextbox(
            target_type="RECEIVED",
            original_message=original_message,
            translated_message=translated_message,
        )


    @staticmethod
    def getTextFromMessageBox():
        return vrct_gui.entry_message_box.get()

    @staticmethod
    def clearMessageBox():
        vrct_gui.entry_message_box.delete(0, CTK_END)

    @staticmethod
    def setMainWindowTransparency(transparency:float):
        vrct_gui.wm_attributes("-alpha", transparency)



    def createGUI(self):
        vrct_gui.createGUI(settings=self.settings, view_variable=self.view_variable)

    @staticmethod
    def startMainLoop():
        vrct_gui.startMainLoop()


    # Config Window
    @staticmethod
    def setConfigWindowCompactModeSwitchStatusToDisabled():
        vrct_gui.config_window.setting_box_compact_mode_switch_box.configure(state="disabled")

    @staticmethod
    def setConfigWindowCompactModeSwitchStatusToNormal():
        vrct_gui.config_window.setting_box_compact_mode_switch_box.configure(state="normal")

    @staticmethod
    def setConfigWindowThresholdCheckWidgetsStatusToDisabled():
        vrct_gui.changeConfigWindowWidgetsStatus(
            status="disabled",
            target_names=[
                "mic_energy_threshold_check_button",
                "speaker_energy_threshold_check_button",
            ]
        )

    @staticmethod
    def setConfigWindowThresholdCheckWidgetsStatusToNormal():
        vrct_gui.changeConfigWindowWidgetsStatus(
            status="normal",
            target_names=[
                "mic_energy_threshold_check_button",
                "speaker_energy_threshold_check_button",
            ]
        )

    @staticmethod
    def replaceConfigWindowMicThresholdCheckButtonToActive():
        vrct_gui.config_window.sb__progressbar_x_slider__passive_button_mic_energy_threshold.grid_remove()
        vrct_gui.config_window.sb__progressbar_x_slider__active_button_mic_energy_threshold.grid()

    @staticmethod
    def replaceConfigWindowMicThresholdCheckButtonToPassive():
        vrct_gui.config_window.sb__progressbar_x_slider__active_button_mic_energy_threshold.grid_remove()
        vrct_gui.config_window.sb__progressbar_x_slider__passive_button_mic_energy_threshold.grid()



    @staticmethod
    def replaceConfigWindowSpeakerThresholdCheckButtonToActive():
        vrct_gui.config_window.sb__progressbar_x_slider__passive_button_speaker_energy_threshold.grid_remove()
        vrct_gui.config_window.sb__progressbar_x_slider__active_button_speaker_energy_threshold.grid()

    @staticmethod
    def replaceConfigWindowSpeakerThresholdCheckButtonToPassive():
        vrct_gui.config_window.sb__progressbar_x_slider__active_button_speaker_energy_threshold.grid_remove()
        vrct_gui.config_window.sb__progressbar_x_slider__passive_button_speaker_energy_threshold.grid()



    @staticmethod
    def reloadConfigWindowSettingBoxContainer():
        vrct_gui.config_window.settings.IS_CONFIG_WINDOW_COMPACT_MODE = config.IS_CONFIG_WINDOW_COMPACT_MODE
        vrct_gui.config_window.reloadConfigWindowSettingBoxContainer()


    def updateList_MicHost(self, new_mic_host_list:list):
        self.view_variable.LIST_MIC_HOST = new_mic_host_list
        vrct_gui.config_window.sb__optionmenu_mic_host.configure(values=new_mic_host_list)

    def updateSelected_MicHost(self, selected_mic_host_name:str):
        self.view_variable.VAR_MIC_HOST.set(selected_mic_host_name)

    def updateList_MicDevice(self, new_mic_device_list):
        self.view_variable.LIST_MIC_DEVICE = new_mic_device_list
        vrct_gui.config_window.sb__optionmenu_mic_device.configure(values=new_mic_device_list)

    def updateSelected_MicDevice(self, default_selected_mic_device_name:str):
        self.view_variable.VAR_MIC_DEVICE.set(default_selected_mic_device_name)

    def updateSetProgressBar_MicEnergy(self, new_mic_energy):
        vrct_gui.config_window.sb__progressbar_x_slider__progressbar_mic_energy_threshold.set(new_mic_energy/config.MAX_MIC_ENERGY_THRESHOLD)

    def updateList_SpeakerDevice(self, new_speaker_device_list):
        self.view_variable.LIST_SPEAKER_DEVICE = new_speaker_device_list
        vrct_gui.config_window.sb__optionmenu_speaker_device.configure(values=new_speaker_device_list)

    def updateSetProgressBar_SpeakerEnergy(self, new_speaker_energy):
        vrct_gui.config_window.sb__progressbar_x_slider__progressbar_speaker_energy_threshold.set(new_speaker_energy/config.MAX_SPEAKER_ENERGY_THRESHOLD)



    def setGuiVariable_MicEnergyThreshold(self, slider_value:int, entry_value:Union[None, str]=None):
        self.view_variable.VAR_MIC_ENERGY_THRESHOLD__SLIDER.set(slider_value)
        if entry_value is None:
            self._clearEntryBox(vrct_gui.config_window.sb__progressbar_x_slider__entry_mic_energy_threshold)
        else:
            self.view_variable.VAR_MIC_ENERGY_THRESHOLD__ENTRY.set(entry_value)

    def setGuiVariable_SpeakerEnergyThreshold(self, slider_value:int, entry_value:Union[None, str]=None):
        self.view_variable.VAR_SPEAKER_ENERGY_THRESHOLD__SLIDER.set(slider_value)
        if entry_value is None:
            self._clearEntryBox(vrct_gui.config_window.sb__progressbar_x_slider__entry_speaker_energy_threshold)
        else:
            self.view_variable.VAR_SPEAKER_ENERGY_THRESHOLD__ENTRY.set(entry_value)



    def setGuiVariable_MicRecordTimeout(self, value:str="", delete=False):
        if delete is True: self._clearEntryBox(vrct_gui.config_window.sb__entry_mic_record_timeout)
        self.view_variable.VAR_MIC_RECORD_TIMEOUT.set(value)

    def setGuiVariable_MicPhraseTimeout(self, value:str="", delete=False):
        if delete is True: self._clearEntryBox(vrct_gui.config_window.sb__entry_mic_phrase_timeout)
        self.view_variable.VAR_MIC_PHRASE_TIMEOUT.set(value)

    def setGuiVariable_MicMaxPhrases(self, value:str="", delete=False):
        if delete is True: self._clearEntryBox(vrct_gui.config_window.sb__entry_mic_max_phrases)
        self.view_variable.VAR_MIC_MAX_PHRASES.set(value)



    def setGuiVariable_SpeakerRecordTimeout(self, value:str="", delete=False):
        if delete is True: self._clearEntryBox(vrct_gui.config_window.sb__entry_speaker_record_timeout)
        self.view_variable.VAR_SPEAKER_RECORD_TIMEOUT.set(value)

    def setGuiVariable_SpeakerPhraseTimeout(self, value:str="", delete=False):
        if delete is True: self._clearEntryBox(vrct_gui.config_window.sb__entry_speaker_phrase_timeout)
        self.view_variable.VAR_SPEAKER_PHRASE_TIMEOUT.set(value)

    def setGuiVariable_SpeakerMaxPhrases(self, value:str="", delete=False):
        if delete is True: self._clearEntryBox(vrct_gui.config_window.sb__entry_speaker_max_phrases)
        self.view_variable.VAR_SPEAKER_MAX_PHRASES.set(value)


    @staticmethod
    def _clearEntryBox(entry_widget):
        entry_widget.delete(0, CTK_END)




    # These conversations are generated by ChatGPT
    def _insertSampleConversationToTextbox(self):

        self.printToTextbox_enableTranscriptionSend()
        self.printToTextbox_enableTranscriptionReceive()

        conversation_data_without_translation = [
            {
                "me": "おはよう。",
            },
            {
                "me": "おはよう。",
                "target": "やぁ。",
            },
            {
                "me": "今日の天気はどうかな？",
                "target": "天気予報を見てないけど、晴れるといいね。",
            },
            {
                "me": "そうだね。昨日は雨だったから。",
                "target": "それで、今日の予定は？",
            },
        ]

        for data in conversation_data_without_translation:
            if data.get("me", None) is not None:
                self.printToTextbox_SentMessage(data.get("me", None), data.get("me_t", None))
            if data.get("target", None) is not None:
                self.printToTextbox_ReceivedMessage(data.get("target", None), data.get("target_t", None))

        self.printToTextbox_enableTranslation()

        conversation_data = [
            {
                "me": "I have work in the morning, but I'm meeting friends for dinner in the evening.",
                "me_t": "아침에 일이 있지만 저녁에 친구들과 만나 저녁 식사할 예정이에요.",
                "target": "재미있어 보여요! 무엇을 먹을 예정이에요?",
                "target_t": "Sounds fun! What are you planning to eat?"
            },
            {
                "me": "We're going to an Italian restaurant, and I'm going to have pizza.",
                "me_t": "우리는 이탈리안 레스토랑에 가서 피자를 먹을 거에요.",
                "target": "그걸 듣자마자 배가 고파져요. 언젠가 함께하고 싶어요.",
                "target_t": "Just hearing that makes me hungry. I'd love to join you sometime."
            },
            {
                "me": "Let's plan it for next time!",
                "me_t": "다음 번에 계획해 봐요!",
                "target": "그래요!",
                "target_t": "Sure!"
            },
            {
                "me": "When would be a good time for you?",
                "me_t": "너에게 언제가 좋을까?",
                "target": "나는 주말이 가장 좋을 것 같아요. 토요일은 어때요?",
                "target_t": "I think the weekend works best for me. How about Saturday?"
            },
            {
                "me": "Saturday sounds perfect. What time would be convenient?",
                "me_t": "토요일이 완벽해 보여. 편한 시간은 언제인가요?",
                "target": "저는 저녁이 괜찮아요. 7시쯤 괜찮을까요?",
                "target_t": "Evening works for me. Is around 7 PM okay?"
            },
            {
                "me": "7 PM works great. Do you have any preferences for food other than Italian?",
                "me_t": "7시가 아주 적당해. 이탈리안 음식 이외에 어떤 음식을 좋아하세요?",
                "target": "특별한 선호도는 없어요. 무엇이든 괜찮아요. 추천 디저트가 있다면 알려주세요.",
                "target_t": "I don't have any particular preferences, so anything is fine. If there's a recommended dessert, let me know."
            },


            {
                "me": "朝は仕事があるけど、夜は友達と食事に行く予定だよ。",
                "me_t": "I have work in the morning, but I'm meeting friends for dinner in the evening.",
                "target": "Sounds fun! What are you planning to eat?",
                "target_t": "楽しそう！何を食べる予定？",
            },
            {
                "me": "イタリアンレストランに行って、ピザを食べるつもりだよ。",
                "me_t": "We're going to an Italian restaurant, and I'm going to have pizza.",
                "target": "Just hearing that makes me hungry. I'd love to join you sometime.",
                "target_t": "それ聞いただけでおなかすいたよ。私も一緒に行きたいな。",
            },
            {
                "me": "次回にぜひ一緒に行こう！",
                "me_t": "Let's plan it for next time!",
                "target": "Sure!",
                "target_t": "そうだね！",
            },
            {
                "me": "次回はいつがいいかな？",
                "me_t": "When would be a good time for you?",
                "target": "I think the weekend works best for me. How about Saturday?",
                "target_t": "私は週末が一番いいかな。土曜日はどう？"
            },
            {
                "me": "土曜日はちょうどいいね。何時ごろが良いかな？",
                "me_t": "Saturday sounds perfect. What time would be convenient?",
                "target": "Evening works for me. Is around 7 PM okay?",
                "target_t": "夜がいいかな。7時くらいからがちょうど良いかな。"
            },
            {
                "me": "7時からはちょうどいいよ。イタリアン以外の食べ物について何か好みがある？",
                "me_t": "7 PM works great. Do you have any preferences for food other than Italian?",
                "target": "I don't have any particular preferences, so anything is fine. If there's a recommended dessert, let me know.",
                "target_t": "特に好みはないから、何でも大丈夫。おすすめのデザートがあれば教えてね。"
            },
        ]
        for data in conversation_data:
            if data.get("me", None) is not None:
                self.printToTextbox_SentMessage(data.get("me", None), data.get("me_t", None))
            if data.get("target", None) is not None:
                self.printToTextbox_ReceivedMessage(data.get("target", None), data.get("target_t", None))


view = View()