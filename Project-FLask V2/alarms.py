import signals


# -------------------------------------- AI TYPE -------------------------------------- #
# ---------- Runtime Hours ---------- #
class RuntimeHours(signals.AI):
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str, **kwargs):
        """ Standard Run Time hours - AI signal  """
        super().__init__(**kwargs)
        self.tag = f"{tag}_XXX_RUNNI_HRS"
        self.description = f"{description} Runtime Hours",
        self.i_o_address = f"{channel_name}.{plc_name}.{tag}.SCADA.RUNNI_HRS",
        self.high_egu_limit = "999,999",
        self.egu_tag = "hrs",
        self.hi_alarm_limit = "999999",
        self.hi_hi_alarm_limit = "999999",
        self.dead_band = "50000",
        self.alarm_area_1 = alarm_area,
        self.scale_high = "999999"


class Alarms:
    def __init__(self, tag: str, description: str, plc_name: str, channel_name: str, alarm_area: str):
        """ This is alarms with specified characteristics  """
        # -------------------------------------- AI TYPE -------------------------------------- #

        # ---------- Runtime Hours ---------- #
        self.runtime_hours = signals.AI(tag=f"{tag}_XXX_RUNNI_HRS",
                                        description=f"{description} Runtime Hours",
                                        i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.RUNNI_HRS",
                                        high_egu_limit="999,999",
                                        egu_tag="hrs",
                                        hi_alarm_limit="999999",
                                        hi_hi_alarm_limit="999999",
                                        dead_band="50000",
                                        alarm_area_1=alarm_area,
                                        scale_high="999999")
        # ---------- tart Counter Total ---------- #
        self.start_counter_total = signals.AI(
            tag=f"{tag}_XXX_STTOT_CRT",
            description=f"{description} Start Counter Total",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.STTOT_CRT.ACC",
            high_egu_limit="999,999",
            egu_tag="Starts",
            hi_alarm_limit="999999",
            hi_hi_alarm_limit="999999",
            dead_band="50000",
            alarm_area_1=alarm_area,
            scale_high="999999")
        # ---------- Start Counter Today ---------- #
        self.start_counter_today = signals.AI(
            tag=f"{tag}_XXX_STTDY_CRT",
            description=f"{description} Start Counter Today",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.STTDY_CRT.ACC",
            high_egu_limit="999,999",
            egu_tag="Starts",
            hi_alarm_limit="999999",
            hi_hi_alarm_limit="999999",
            dead_band="50000",
            alarm_area_1=alarm_area,
            scale_high="999999")
        # ---------- Start Counter Month ---------- #
        self.start_counter_month = signals.AI(
            tag=f"{tag}_XXX_STMTH_CRT",
            description=f"{description} Start Counter Month",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.STMTH_CRT.ACC",
            high_egu_limit="999,999",
            egu_tag="Starts",
            hi_alarm_limit="999999",
            hi_hi_alarm_limit="999999",
            dead_band="50000",
            alarm_area_1=alarm_area,
            scale_high="999999")
        # ---------- Speed CV ---------- #
        self.speed_cv = signals.AI(
            tag=f"{tag}_SI1_STAAI_CV",
            description=f"{description} Speed CV",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.CV",
            high_egu_limit="100",
            egu_tag="%",
            hi_alarm_limit="100",
            hi_hi_alarm_limit="100",
            dead_band="5",
            alarm_area_1=alarm_area,
            scale_high="100")
        # ---------- Speed mA Value ---------- #
        self.speed_ma_value = signals.AI(
            tag=f"{tag}_SI1_STAAI_MA",
            description=f"{description} Speed mA Value",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.MA",
            low_egu_limit="4",
            high_egu_limit="20",
            egu_tag="mA",
            lo_alarm_limit="4",
            lo_lo_alarm_limit="4",
            hi_alarm_limit="20",
            hi_hi_alarm_limit="20",
            dead_band="1",
            alarm_area_1=alarm_area,
            scale_low="4",
            scale_high="20")
        # ---------- Speed Speed PCT ---------- #
        self.speed_pct = signals.AI(
            tag=f"{tag}_SI1_STAAI_PCT",
            description=f"{description} Speed PCT",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.PCT",
            high_egu_limit="100",
            egu_tag="%",
            hi_alarm_limit="100",
            hi_hi_alarm_limit="100",
            dead_band="5",
            alarm_area_1=alarm_area,
            scale_high="100")
        # ---------- Speed Alarm Severity ---------- #
        self.speed_alarm_severity = signals.AI(
            tag=f"{tag}_SI1_ALARM_SEV",
            description=f"{description} Speed Alarm Severity",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.ALARM_SEV",
            high_egu_limit="3",
            hi_alarm_limit="3",
            hi_hi_alarm_limit="3",
            dead_band="0",
            alarm_area_1=alarm_area,
            scale_high="3")
        # -------------------------------------- DI TYPE -------------------------------------- #

        # ---------- Auto Mode ---------- #
        self.auto_mode = signals.DI(
            tag=f"{tag}_ZS1_AUTOM_STS",
            description=f"{description} Auto Mode",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.ZS1_AUTOM_STS",
            scan_time="10",
            open_tag="OTHER",
            close_tag="AUTO",
            alarm_enable="ENABLE",
            event_messages="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.auto_mode_vfd_pump = self.auto_mode
        self.auto_mode_vfd_pump.scan_time = "3"
        self.auto_mode_vfd_pump.alarm_enable = "DISABLE"
        self.auto_mode_vfd_pump.event_messages = "DISABLE"
        # ---------- Remote Mode ---------- #
        self.remote_mode = signals.DI(
            tag=f"{tag}_ZS1_REMOT_STS",
            description=f"{description} Remote STS",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.ZS1_REMOT_STS",
            scan_time="10",
            open_tag="LOCAL",
            close_tag="REMOTE",
            alarm_enable="ENABLE",
            event_messages="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.remote_mode_vfd_pump = self.remote_mode
        self.remote_mode_vfd_pump.scan_time = "3"
        self.remote_mode_vfd_pump.alarm_enable = "DISABLE"
        self.remote_mode_vfd_pump.event_messages = "DISABLE"
        # ---------- Manual Mode ---------- #
        self.manual_mode = signals.DI(
            tag=f"{tag}_ZS1_MANLM_STS",
            description=f"{description} Manual Mode",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.ZS1_MANLM_STS",
            scan_time="10",
            open_tag="OTHER",
            close_tag="MANUAL",
            alarm_enable="ENABLE",
            event_messages="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.manual_mode_vfd_pump = self.manual_mode
        self.manual_mode_vfd_pump.scan_time = "3"
        self.manual_mode_vfd_pump.alarm_enable = "DISABLE"
        self.manual_mode_vfd_pump.event_messages = "DISABLE"
        # ---------- Running Status ---------- #
        self.running_status = signals.DI(
            tag=f"{tag}_XXX_RUNNG_STS",
            description=f"{description} Running Status",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.RUNNG_STS",
            scan_time="10",
            open_tag="OFF",
            close_tag="RUNNING",
            alarm_enable="ENABLE",
            event_messages="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.running_status_vfd_pump = self.running_status
        self.running_status_vfd_pump.scan_time = "3"
        self.running_status_vfd_pump.alarm_enable = "DISABLE"
        self.running_status_vfd_pump.event_messages = "DISABLE"
        # ---------- Power On Delay ---------- #
        self.power_on_delay = signals.DI(
            tag=f"{tag}_RVS_HTALM_STS",
            description=f"{description} Power On Delay",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_RVS_HTALM_STS",
            scan_time="10",
            open_tag="OFF",
            close_tag="ON",
            alarm_enable="ENABLE",
            event_messages="ENABLE",
            alarm_area_1=alarm_area,
        )
        # ---------- Ready Status ---------- #
        self.ready_status = signals.DI(
            tag=f"{tag}_XXX_READY_STS",
            description=f"{description} Ready Status",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.AVBLE_STS",
            scan_time="3",
            open_tag="LOCAL",
            close_tag="REMOTE",
            alarm_area_1=alarm_area,
        )

        # -------------------------------------- AR TYPE -------------------------------------- #

        # ---------- Speed HIHI Setpoint ---------- #
        self.hi_hi_setpoint = signals.AR(
            tag=f"{tag}_SI1_SETPT_HH",
            description=f"{description} Speed HIHI Setpoint",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.SETPT_HH",
            high_egu_limit="100",
            egu_tag="%",
            enable_output="YES",
        )
        # ---------- Speed HI Setpoint ---------- #
        self.hi_setpoint = signals.AR(
            tag=f"{tag}_SI1_SETPT_HI",
            description=f"{description} Speed HI Setpoint",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.SETPT_HI",
            high_egu_limit="100",
            egu_tag="%",
            enable_output="YES",
        )
        # ---------- Speed Low Setpoint ---------- #
        self.low_setpoint = signals.AR(
            tag=f"{tag}_SI1_SETPT_LO",
            description=f"{description} Speed LO Setpoint",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.SETPT_LO",
            high_egu_limit="100",
            egu_tag="%",
            enable_output="YES",
        )
        # ---------- Speed Low Low Setpoint ---------- #
        self.low_low_setpoint = signals.AR(
            tag=f"{tag}_SI1_SETPT_LL",
            description=f"{description} Speed LOLO Setpoint",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.SETPT_LL",
            high_egu_limit="100",
            egu_tag="%",
            enable_output="YES",
        )
        # ---------- Speed Deadband ---------- #
        self.speed_deadband = signals.AR(
            tag=f"{tag}_SI1_SIGDB_REQ",
            description=f"{description} Speed Deadband",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.SIGDB_REQ",
            high_egu_limit="1",
            scale_high="1",
        )
        # ---------- Centman Speed ---------- #
        self.centman_speed = signals.AR(
            tag=f"{tag}_XXX_SETPT_MAN",
            description=f"{description} Centman Speed",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.SETPT_MAN",
            high_egu_limit="100",
            egu_tag="%",
            enable_output="YES",
        )

        # -------------------------------------- DR TYPE -------------------------------------- #

        # ---------- Run Time Reset ---------- #
        self.runtime_reset = signals.DR(
            tag=f"{tag}_XXX_RNTME_RST",
            description=f"{description} Run Time Reset",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.RNTME_RST",
            enable_output="YES",
            open_tag="OFF",
            close_tag="RESET",
        )
        # -- VFD PUMP -- #
        self.runtime_reset_vfd_pump = self.runtime_reset
        self.runtime_reset_vfd_pump.open_tag = "DISABLE"
        self.runtime_reset_vfd_pump.close_tag = "ENABLE"
        self.runtime_reset_vfd_pump.event_messages = "ENABLE"
        # ---------- Out of Service ---------- #
        self.out_service = signals.DR(
            tag=f"{tag}_XXX_OUTSV_STS",
            description=f"{description} Out of Service",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.ZS1_OUTSV_STS",
            enable_output="YES",
            open_tag="DISABLE",
            close_tag="ENABLE",
            event_messages="ENABLE",
        )
        # ---------- Manual Start Request ---------- #
        self.manual_start_req = signals.DR(
            tag=f"{tag}_XXX_MANST_REQ",
            description=f"{description} Manual Start Request",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.MANST_REQ",
            enable_output="YES",
            open_tag="OFF",
            close_tag="START",
        )
        # ---------- Manual Stop Request ---------- #
        self.manual_stop_req = signals.DR(
            tag=f"{tag}_XXX_MANSP_REQ",
            description=f"{description} Manual Stop Request",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.MANSP_REQ",
            enable_output="YES",
            open_tag="OFF",
            close_tag="STOP",
        )
        # ---------- Manual Mode Request ---------- #
        self.manual_mode_req = signals.DR(
            tag=f"{tag}_XXX_MANLM_REQ",
            description=f"{description} Manual Mode Request",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.MANLM_REQ",
            enable_output="YES",
            open_tag="AUTO",
            close_tag="MANUAL",
        )
        # ---------- Auto Mode Request ---------- #
        self.auto_mode_req = signals.DR(
            tag=f"{tag}_XXX_AUTOM_REQ",
            description=f"{description} Auto Mode Request",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.AUTOM_REQ",
            enable_output="YES",
            open_tag="OPEN",
            close_tag="CLOSE",
        )
        # ---------- Alarm Acknowledge ---------- #
        self.alarm_ack = signals.DR(
            tag=f"{tag}_XXX_ALARM_ACK",
            description=f"{description} Alarm Acknowledge",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.ALARM_ACK",
            enable_output="YES",
            open_tag="OFF",
            close_tag="ACK",
        )
        # ---------- Backup Reset ---------- #
        self.backup_reset = signals.DR(
            tag=f"{tag}_XXX_BCKUP_RST",
            description=f"{description} Backup Reset",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.BCKUP_RST",
            enable_output="YES",
            open_tag="OPEN",
            close_tag="CLOSE",
        )
        # ---------- Speed HIHI Alarm Enable ---------- #
        self.speed_hi_hi_alarm_enable = signals.DR(
            tag=f"{tag}_SI1_HHALM_ENB",
            description=f"{description} Spd HIHI Alm EN",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.HHALM_ENB",
            enable_output="YES",
            open_tag="DISABLE",
            close_tag="ENABLE",
        )
        # ---------- Speed HI Alarm Enable ---------- #
        self.speed_hi_alarm_enable = signals.DR(
            tag=f"{tag}_SI1_HIALM_ENB",
            description=f"{description} Spd HI Alm EN",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.HIALM_ENB",
            enable_output="YES",
            open_tag="DISABLE",
            close_tag="ENABLE",
        )
        # ---------- Speed Low Low Alarm Enable ---------- #
        self.speed_low_low_alarm_enable = signals.DR(
            tag=f"{tag}_SI1_LLALM_ENB",
            description=f"{description} Spd LOLO Alm EN",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.LLALM_ENB",
            enable_output="YES",
            open_tag="DISABLE",
            close_tag="ENABLE",
        )
        # ---------- Speed Low  Alarm Enable ---------- #
        self.speed_low_alarm_enable = signals.DR(
            tag=f"{tag}_SI1_LOALM_ENB",
            description=f"{description} Spd LO Alm EN",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.LOALM_ENB",
            enable_output="YES",
            open_tag="DISABLE",
            close_tag="ENABLE",
        )
        # ---------- Speed Maintenance Mode Enable ---------- #
        self.maintenance_mode_enable = signals.DR(
            tag=f"{tag}_SI1_MAINT_ENB",
            description=f"{description} Spd Maint Mode En",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.MAINT_ENB",
            enable_output="YES",
            open_tag="DISABLE",
            close_tag="ENABLE",
        )
        # -------------------------------------- DA TYPE -------------------------------------- #

        # ---------- Fail To Start Alarm ---------- #
        self.fail_start_alarm = signals.DA(
            tag=f"{tag}_XXX_FLSTR_ALM",
            description=f"{description} Fail To Start Alarm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.FLSTR_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.fail_start_alarm_vfd_pump = self.fail_start_alarm
        self.fail_start_alarm_vfd_pump.alarm_priority = "High"
        # ---------- Fail To Stop Alarm ---------- #
        self.fail_stop_alarm = signals.DA(
            tag=f"{tag}_XXX_FLSTP_ALM",
            description=f"{description} Fail To Stop Alarm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.FLSTP_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.fail_stop_alarm_vfd_pump = self.fail_stop_alarm
        self.fail_stop_alarm_vfd_pump.alarm_priority = "High"
        # ---------- Uncommanded Start Alarm ---------- #
        self.uncommand_start_alarm = signals.DA(
            tag=f"{tag}_XXX_UCSTR_ALM",
            description=f"{description} Uncommand. Start Alm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.UCSTR_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.uncommand_start_alarm_vfd_pump = self.uncommand_start_alarm
        self.uncommand_start_alarm_vfd_pump.alarm_priority = "High"
        # ---------- Uncommanded Stop Alarm ---------- #
        self.uncommand_stop_alarm = signals.DA(
            tag=f"{tag}_XXX_UCSTP_ALM",
            description=f"{description} Uncommand. Stop Alm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.UCSTP_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.uncommand_stop_alarm_vfd_pump = self.uncommand_stop_alarm
        self.uncommand_stop_alarm_vfd_pump.alarm_priority = "High"
        # ---------- General Alarm ---------- #
        self.general_alarm = signals.DA(
            tag=f"{tag}_XXX_GENAL_ALM",
            description=f"{description} General Alarm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.GENAL_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.general_alarm_vfd_pump = self.general_alarm
        self.general_alarm_vfd_pump.alarm_priority = "High"
        # ---------- Start Float Alarm ---------- #
        self.start_float_alarm = signals.DA(
            tag=f"{tag}_XXX_SRTLS_ALM",
            description=f"{description} Start Float Alarm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.SRTLS_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # ---------- ON Float Alarm ---------- #
        self.on_float_alarm = signals.DA(
            tag=f"{tag}_XXX_ONFLT_ALM",
            description=f"{description} On Float Alarm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.ONFLT_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # ---------- Soft Starter Fault Alarm ---------- #
        self.soft_started_fault_alarm = signals.DA(
            tag=f"{tag}_RVS_FAULT_ALM",
            description=f"{description} Soft Starter Fault Alm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.FAULT_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # ---------- Temp/Leakage Alarm ---------- #
        self.temp_leak_alarm = signals.DA(
            tag=f"{tag}_XXX_TMPLK_ALM",
            description=f"{description} Temp/Leakage Alarm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.TMPLK_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.temp_leak_alarm_vfd_pump = self.temp_leak_alarm
        self.temp_leak_alarm_vfd_pump.alarm_priority = "High"
        # ---------- Speed Dev Alarm ---------- #
        self.speed_dev_alarm = signals.DA(
            tag=f"{tag}_XXX_SPDDV_ALM",
            description=f"{description} Speed Dev Alarm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.SPDDV_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.speed_dev_alarm_vfd_pump = self.speed_dev_alarm
        self.speed_dev_alarm_vfd_pump.alarm_priority = "High"
        # ---------- VFD FAULT Alarm ---------- #
        self.vfd_fault_alarm = signals.DA(
            tag=f"{tag}_XXX_FAULT_ALM",
            description=f"{description} VFD Fault Alm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}.SCADA.FAULT_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.vfd_fault_alarm_vfd_pump = self.vfd_fault_alarm
        self.vfd_fault_alarm_vfd_pump.alarm_priority = "High"
        # ---------- Speed HIHI Alarm ---------- #
        self.speed_hi_hi_alarm = signals.DA(
            tag=f"{tag}_SI1_STAHH_ALM",
            description=f"{description} Speed HIHI Alarm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.STAHH_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.speed_hi_hi_alarm_vfd_pump = self.speed_hi_hi_alarm
        self.speed_hi_hi_alarm_vfd_pump.alarm_priority = "High"
        # ---------- Speed HIHI Alarm ---------- #
        self.speed_hi_alarm = signals.DA(
            tag=f"{tag}_SI1_STAHI_ALM",
            description=f"{description} Speed HI Alarm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.STAHI_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.speed_hi_alarm_vfd_pump = self.speed_hi_alarm
        self.speed_hi_alarm_vfd_pump.alarm_priority = "High"
        # ---------- Speed Low Low Alarm ---------- #
        self.speed_low_low_alarm = signals.DA(
            tag=f"{tag}_SI1_STALL_ALM",
            description=f"{description} Speed LOLO Alarm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.STALL_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.speed_low_low_alarm_vfd_pump = self.speed_low_low_alarm
        self.speed_low_low_alarm_vfd_pump.alarm_priority = "High"
        # ---------- Speed Low  Alarm ---------- #
        self.speed_low_alarm = signals.DA(
            tag=f"{tag}_SI1_STALO_ALM",
            description=f"{description} Speed LO Alarm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.STALO_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.speed_low_alarm_vfd_pump = self.speed_low_alarm
        self.speed_low_alarm_vfd_pump.alarm_priority = "High"
        # ---------- Speed Maintenance  Alarm ---------- #
        self.speed_maintenance_mode_alarm = signals.DA(
            tag=f"{tag}_SI1_MAINT_ALM",
            description=f"{description} Spd Maint Mode Alm",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.MAINT_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.speed_maintenance_mode_alarm_vfd_pump = self.speed_maintenance_mode_alarm
        self.speed_maintenance_mode_alarm_vfd_pump.alarm_priority = "High"
        # ---------- Speed Signal  Error Alarm ---------- #
        self.speed_signal_error_alarm = signals.DA(
            tag=f"{tag}_SI1_SIGNL_ALM",
            description=f"{description} Speed Signal Error",
            i_o_address=f"{channel_name}.{plc_name}.{tag}_SI1.SCADA.SIGNL_ALM",
            scan_time="10",
            open_tag="NORMAL",
            close_tag="ALARM",
            alarm_enable="ENABLE",
            alarm_area_1=alarm_area,
        )
        # -- VFD PUMP -- #
        self.speed_signal_error_alarm_vfd_pump = self.speed_signal_error_alarm
        self.speed_maintenance_mode_alarm_vfd_pump.alarm_priority = "High"
