from flask_wtf import Form
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired, Email


class Form1Form(Form):
    # actual
    actual_1 = StringField("actual_1", validators=[DataRequired()])
    actual_2 = StringField("actual_2", validators=[DataRequired()])
    actual_3 = StringField("actual_3", validators=[DataRequired()])
    actual_4 = StringField("actual_4", validators=[DataRequired()])
    actual_5 = StringField("actual_5", validators=[DataRequired()])
    actual_6 = StringField("actual_6", validators=[DataRequired()])
    actual_7 = StringField("actual_7", validators=[DataRequired()])
    actual_8 = StringField("actual_8", validators=[DataRequired()])
    actual_total = StringField("actual_total", validators=[DataRequired()])

    # top 3 reasons
    #  t3r_1 = StringField('top3r_1', validators=[DataRequired()])
    #  t3r_2 = StringField('top3r_2', validators=[DataRequired()])
    #  t3r_3 = StringField('top3r_3', validators=[DataRequired()])
    t3r_4 = StringField("top3r_4", validators=[DataRequired()])
    t3r_5 = StringField("top3r_5", validators=[DataRequired()])
    t3r_6 = StringField("top3r_6", validators=[DataRequired()])
    t3r_7 = StringField("top3r_7", validators=[DataRequired()])
    t3r_8 = StringField("top3r_8", validators=[DataRequired()])
    t3r_total = StringField("top3r_total", validators=[DataRequired()])

    # unloaded
    unloaded_1 = StringField("unloaded_1", validators=[DataRequired()])
    unloaded_2 = StringField("unloaded_2", validators=[DataRequired()])
    unloaded_3 = StringField("unloaded_3", validators=[DataRequired()])
    unloaded_4 = StringField("unloaded_4", validators=[DataRequired()])
    unloaded_5 = StringField("unloaded_5", validators=[DataRequired()])
    unloaded_6 = StringField("unloaded_6", validators=[DataRequired()])
    unloaded_7 = StringField("unloaded_7", validators=[DataRequired()])
    unloaded_8 = StringField("unloaded_8", validators=[DataRequired()])
    unloaded_total = StringField("unloaded_total", validators=[DataRequired()])

    # ok
    ok_1 = StringField("ok_1", validators=[DataRequired()])
    ok_2 = StringField("ok_2", validators=[DataRequired()])
    ok_3 = StringField("ok_3", validators=[DataRequired()])
    ok_4 = StringField("ok_4", validators=[DataRequired()])
    ok_5 = StringField("ok_5", validators=[DataRequired()])
    ok_6 = StringField("ok_6", validators=[DataRequired()])
    ok_7 = StringField("ok_7", validators=[DataRequired()])
    ok_8 = StringField("ok_8", validators=[DataRequired()])
    ok_total = StringField("ok_total", validators=[DataRequired()])

    # rejected
    rejected_1 = StringField("rejected_1", validators=[DataRequired()])
    rejected_2 = StringField("rejected_2", validators=[DataRequired()])
    rejected_3 = StringField("rejected_3", validators=[DataRequired()])
    rejected_4 = StringField("rejected_4", validators=[DataRequired()])
    rejected_5 = StringField("rejected_5", validators=[DataRequired()])
    rejected_6 = StringField("rejected_6", validators=[DataRequired()])
    rejected_7 = StringField("rejected_7", validators=[DataRequired()])
    rejected_8 = StringField("rejected_8", validators=[DataRequired()])
    rejected_total = StringField("rejected_total", validators=[DataRequired()])

    # RD
    rd_1 = StringField("rd_1", validators=[DataRequired()])
    rd_2 = StringField("rd_2", validators=[DataRequired()])
    rd_3 = StringField("rd_3", validators=[DataRequired()])
    rd_4 = StringField("rd_4", validators=[DataRequired()])
    rd_5 = StringField("rd_5", validators=[DataRequired()])
    rd_6 = StringField("rd_6", validators=[DataRequired()])
    rd_7 = StringField("rd_7", validators=[DataRequired()])
    rd_8 = StringField("rd_8", validators=[DataRequired()])
    rd_total = StringField("rd_total", validators=[DataRequired()])

    # dust
    dust_1 = StringField("dust_1", validators=[DataRequired()])
    dust_2 = StringField("dust_2", validators=[DataRequired()])
    dust_3 = StringField("dust_3", validators=[DataRequired()])
    dust_4 = StringField("dust_4", validators=[DataRequired()])
    dust_5 = StringField("dust_5", validators=[DataRequired()])
    dust_6 = StringField("dust_6", validators=[DataRequired()])
    dust_7 = StringField("dust_7", validators=[DataRequired()])
    dust_8 = StringField("dust_8", validators=[DataRequired()])
    dust_total = StringField("dust_total", validators=[DataRequired()])

    # RD
    rd_1 = StringField("rd_1", validators=[DataRequired()])
    rd_2 = StringField("rd_2", validators=[DataRequired()])
    rd_3 = StringField("rd_3", validators=[DataRequired()])
    rd_4 = StringField("rd_4", validators=[DataRequired()])
    rd_5 = StringField("rd_5", validators=[DataRequired()])
    rd_6 = StringField("rd_6", validators=[DataRequired()])
    rd_7 = StringField("rd_7", validators=[DataRequired()])
    rd_8 = StringField("rd_8", validators=[DataRequired()])
    rd_total = StringField("rd_total", validators=[DataRequired()])

    # UC
    uc_1 = StringField("uc_1", validators=[DataRequired()])
    uc_2 = StringField("uc_2", validators=[DataRequired()])
    uc_3 = StringField("uc_3", validators=[DataRequired()])
    uc_4 = StringField("uc_4", validators=[DataRequired()])
    uc_5 = StringField("uc_5", validators=[DataRequired()])
    uc_6 = StringField("uc_6", validators=[DataRequired()])
    uc_7 = StringField("uc_7", validators=[DataRequired()])
    uc_8 = StringField("uc_8", validators=[DataRequired()])
    uc_total = StringField("uc_total", validators=[DataRequired()])

    # DSPRAY
    dspray_1 = StringField("dspray_1", validators=[DataRequired()])
    dspray_2 = StringField("dspray_2", validators=[DataRequired()])
    dspray_3 = StringField("dspray_3", validators=[DataRequired()])
    dspray_4 = StringField("dspray_4", validators=[DataRequired()])
    dspray_5 = StringField("dspray_5", validators=[DataRequired()])
    dspray_6 = StringField("dspray_6", validators=[DataRequired()])
    dspray_7 = StringField("dspray_7", validators=[DataRequired()])
    dspray_8 = StringField("dspray_8", validators=[DataRequired()])
    dspray_total = StringField("dspray_total", validators=[DataRequired()])

    # SPITT
    spitt_1 = StringField("spitt_1", validators=[DataRequired()])
    spitt_2 = StringField("spitt_2", validators=[DataRequired()])
    spitt_3 = StringField("spitt_3", validators=[DataRequired()])
    spitt_4 = StringField("spitt_4", validators=[DataRequired()])
    spitt_5 = StringField("spitt_5", validators=[DataRequired()])
    spitt_6 = StringField("spitt_6", validators=[DataRequired()])
    spitt_7 = StringField("spitt_7", validators=[DataRequired()])
    spitt_8 = StringField("spitt_8", validators=[DataRequired()])
    spitt_total = StringField("spitt_total", validators=[DataRequired()])

    # OThers
    others_1 = StringField("others_1", validators=[DataRequired()])
    others_2 = StringField("others_2", validators=[DataRequired()])
    others_3 = StringField("others_3", validators=[DataRequired()])
    others_4 = StringField("others_4", validators=[DataRequired()])
    others_5 = StringField("others_5", validators=[DataRequired()])
    others_6 = StringField("others_6", validators=[DataRequired()])
    others_7 = StringField("others_7", validators=[DataRequired()])
    others_8 = StringField("others_8", validators=[DataRequired()])
    others_total = StringField("others_total", validators=[DataRequired()])

    reg = StringField("reg", validators=[DataRequired()])
    cl = StringField("cl", validators=[DataRequired()])
    plan = StringField("plan", validators=[DataRequired()])
    faid = StringField("faid", validators=[DataRequired()])
    nmiss = StringField("nmiss", validators=[DataRequired()])

    breakdowndetails = StringField("breakdowndetails", validators=[DataRequired()])
    shortcommunication = StringField(
        "shortagecommunication", validators=[DataRequired()]
    )
    feedback = StringField("feedback", validators=[DataRequired()])
    teamleadersign = StringField("teamleadersign", validators=[DataRequired()])
    groupleadersign = StringField("groupleadersign", validators=[DataRequired()])

    # standupmeetings
    standup_p = StringField("standup_p", validators=[DataRequired()])
    standup_q = StringField("standup_q", validators=[DataRequired()])
    standup_c = StringField("standup_c", validators=[DataRequired()])
    standup_d = StringField("standup_d", validators=[DataRequired()])
    standup_m = StringField("standup_m", validators=[DataRequired()])
    standup_s = StringField("standup_s", validators=[DataRequired()])


class Form2Form(Form):
    # first hour output plan
    firstHourOutput_plan_1 = StringField(
        "firstHourOutput_plan_1", validators=[DataRequired()]
    )
    firstHourOutput_plan_2 = StringField(
        "firstHourOutput_plan_2", validators=[DataRequired()]
    )
    firstHourOutput_plan_3 = StringField(
        "firstHourOutput_plan_3", validators=[DataRequired()]
    )

    # first hour output actual
    firstHourOutput_actual_1 = StringField(
        "firstHourOutput_actual_1", validators=[DataRequired()]
    )
    firstHourOutput_actual_2 = StringField(
        "firstHourOutput_actual_2", validators=[DataRequired()]
    )
    firstHourOutput_actual_3 = StringField(
        "firstHourOutput_actual_3", validators=[DataRequired()]
    )

    # first hour output top 3 reasons
    firstHourOutput_top3reasons_1 = StringField(
        "firstHourOutput_top3reasons_1", validators=[DataRequired()]
    )
    firstHourOutput_top3reasons_2 = StringField(
        "firstHourOutput_top3reasons_2", validators=[DataRequired()]
    )

    # first hour output action
    firstHourOutput_action_1 = StringField(
        "firstHourOutput_action_1", validators=[DataRequired()]
    )
    firstHourOutput_action_2 = StringField(
        "firstHourOutput_action_2", validators=[DataRequired()]
    )

    # line stopper plan
    linestopper_plan_1 = StringField("linestopper_plan_1", validators=[DataRequired()])
    linestopper_plan_2 = StringField("linestopper_plan_2", validators=[DataRequired()])
    linestopper_plan_3 = StringField("linestopper_plan_3", validators=[DataRequired()])
    linestopper_plan_4 = StringField("linestopper_plan_4", validators=[DataRequired()])
    linestopper_plan_5 = StringField("linestopper_plan_5", validators=[DataRequired()])
    linestopper_plan_6 = StringField("linestopper_plan_6", validators=[DataRequired()])

    # line stopper actual
    linestopper_actual_1 = StringField(
        "linestopper_actual_1", validators=[DataRequired()]
    )
    linestopper_actual_2 = StringField(
        "linestopper_actual_2", validators=[DataRequired()]
    )
    linestopper_actual_3 = StringField(
        "linestopper_actual_3", validators=[DataRequired()]
    )
    linestopper_actual_4 = StringField(
        "linestopper_actual_4", validators=[DataRequired()]
    )
    linestopper_actual_5 = StringField(
        "linestopper_actual_5", validators=[DataRequired()]
    )
    linestopper_actual_6 = StringField(
        "linestopper_actual_6", validators=[DataRequired()]
    )

    # line stopper top 3 reasons
    linestopper_top3reasons_1 = StringField(
        "linestopper_top3reasons_1", validators=[DataRequired()]
    )
    linestopper_top3reasons_2 = StringField(
        "linestopper_top3reasons_2", validators=[DataRequired()]
    )
    linestopper_top3reasons_3 = StringField(
        "linestopper_top3reasons_3", validators=[DataRequired()]
    )
    linestopper_top3reasons_4 = StringField(
        "linestopper_top3reasons_4", validators=[DataRequired()]
    )
    linestopper_top3reasons_5 = StringField(
        "linestopper_top3reasons_5", validators=[DataRequired()]
    )
    linestopper_top3reasons_6 = StringField(
        "linestopper_top3reasons_6", validators=[DataRequired()]
    )

    # line stopper actual
    linestopper_action_1 = StringField(
        "linestopper_action_1", validators=[DataRequired()]
    )
    linestopper_action_2 = StringField(
        "linestopper_action_2", validators=[DataRequired()]
    )
    linestopper_action_3 = StringField(
        "linestopper_action_3", validators=[DataRequired()]
    )
    linestopper_action_4 = StringField(
        "linestopper_action_4", validators=[DataRequired()]
    )
    linestopper_action_5 = StringField(
        "linestopper_action_5", validators=[DataRequired()]
    )
    linestopper_action_6 = StringField(
        "linestopper_action_6", validators=[DataRequired()]
    )

    # team leader adherence name and p/a
    teamleader_name_1 = StringField("teamleader_name_1", validators=[DataRequired()])
    teamleader_name_2 = StringField("teamleader_name_2", validators=[DataRequired()])
    teamleader_name_3 = StringField("teamleader_name_3", validators=[DataRequired()])
    teamleader_pa_1 = StringField("teamleader_p/a_1", validators=[DataRequired()])
    teamleader_pa_2 = StringField("teamleader_p/a_2", validators=[DataRequired()])
    teamleader_pa_3 = StringField("teamleader_p/a_3", validators=[DataRequired()])

    # CONVEYOR UTILISATION plan
    conveyor_plan_1 = StringField("conveyor_plan_1", validators=[DataRequired()])
    conveyor_plan_2 = StringField("conveyor_plan_2", validators=[DataRequired()])
    conveyor_plan_3 = StringField("conveyor_plan_3", validators=[DataRequired()])
    conveyor_plan_4 = StringField("conveyor_plan_4", validators=[DataRequired()])
    conveyor_plan_5 = StringField("conveyor_plan_5", validators=[DataRequired()])

    # CONVEYOR UTILISATION actual
    conveyor_actual_1 = StringField("conveyor_actual_1", validators=[DataRequired()])
    conveyor_actual_2 = StringField("conveyor_actual_2", validators=[DataRequired()])
    conveyor_actual_3 = StringField("conveyor_actual_3", validators=[DataRequired()])
    conveyor_actual_4 = StringField("conveyor_actual_4", validators=[DataRequired()])
    conveyor_actual_5 = StringField("conveyor_actual_5", validators=[DataRequired()])

    # CONVEYOR UTILISATION top 3 reasons
    conveyor_top3reasons_1 = StringField(
        "conveyor_top3reasonsl_1", validators=[DataRequired()]
    )
    conveyor_top3reasons_2 = StringField(
        "conveyor_top3reasons_2", validators=[DataRequired()]
    )
    conveyor_top3reasons_3 = StringField(
        "conveyor_top3reasons_3", validators=[DataRequired()]
    )

    # CONVEYOR UTILISATION action
    conveyor_action_1 = StringField("conveyor_action_1", validators=[DataRequired()])
    conveyor_action_2 = StringField("conveyor_action_2", validators=[DataRequired()])
    conveyor_action_3 = StringField("conveyor_action_3", validators=[DataRequired()])

    # Absentism
    absent1 = StringField("absent1", validators=[DataRequired()])
    absent2 = StringField("absent2", validators=[DataRequired()])
    absent3 = StringField("absent3", validators=[DataRequired()])

    # safety incident
    safe1 = StringField("safe1", validators=[DataRequired()])
    safe2 = StringField("safe2", validators=[DataRequired()])
    safe3 = StringField("safe3", validators=[DataRequired()])

    # opening stock details
    stock_con300_1 = StringField("stock_con300_1", validators=[DataRequired()])
    stock_con400_1 = StringField("stock_con400_1", validators=[DataRequired()])
    stock_con600_1 = StringField("stock_con600_1", validators=[DataRequired()])
    stock_con300_2 = StringField("stock_con300_2", validators=[DataRequired()])
    stock_con400_2 = StringField("stock_con400_2", validators=[DataRequired()])
    stock_con600_3 = StringField("stock_con600_2", validators=[DataRequired()])
    stock_con300_3 = StringField("stock_con300_3", validators=[DataRequired()])
    stock_con400_3 = StringField("stock_con400_3", validators=[DataRequired()])
    stock_con600_3 = StringField("stock_con600_3", validators=[DataRequired()])

    # leader sign
    groupleadersign = StringField("groupleadersign", validators=[DataRequired()])
    unitmanagersign = StringField("unitmanagersignsign", validators=[DataRequired()])

    # rework plan
    rework_plan_1 = StringField("rework_plan_1", validators=[DataRequired()])
    rework_plan_2 = StringField("rework_plan_2", validators=[DataRequired()])
    rework_plan_3 = StringField("rework_plan_3", validators=[DataRequired()])
    rework_plan_4 = StringField("rework_plan_4", validators=[DataRequired()])
    rework_plan_5 = StringField("rework_plan_5", validators=[DataRequired()])

    # rework actual
    rework_actual_1 = StringField("rework_actual_1", validators=[DataRequired()])
    rework_actual_2 = StringField("rework_actual_2", validators=[DataRequired()])
    rework_actual_3 = StringField("rework_actual_3", validators=[DataRequired()])
    rework_actual_4 = StringField("rework_actual_4", validators=[DataRequired()])
    rework_actual_5 = StringField("rework_actual_5", validators=[DataRequired()])

    # rework top3reasons
    rework_top3reasons_1 = StringField(
        "rework_top3reasons_1", validators=[DataRequired()]
    )
    rework_top3reasons_2 = StringField(
        "rework_top3reasons_2", validators=[DataRequired()]
    )
    rework_top3reasons_3 = StringField(
        "rework_top3reasons_3", validators=[DataRequired()]
    )

    # rework actual
    rework_action_1 = StringField("rework_action_1", validators=[DataRequired()])
    rework_action_2 = StringField("rework_action_2", validators=[DataRequired()])
    rework_action_3 = StringField("rework_action_3", validators=[DataRequired()])

    # actually done
    actuallydone_status = StringField(
        "actuallydone_status", validators=[DataRequired()]
    )

    # feedback
    breakdown = StringField("breakdown", validators=[DataRequired()])

    # breakdown
    feedback = StringField("feedback", validators=[DataRequired()])

    # spare quantity
    sparequantity_plan = StringField("sparequantity_plan", validators=[DataRequired()])
    sparequantity_actual = StringField(
        "sparequantity_actual", validators=[DataRequired()]
    )

    # REWORK PARTS STATUS plan
    reworkpart_plan_1 = StringField("reworkpart_plan_1", validators=[DataRequired()])

    # REWORK PARTS STATUS sanded
    reworkpart_sanded_1 = StringField(
        "reworkpart_sanded_1", validators=[DataRequired()]
    )
    reworkpart_sanded_2a = StringField(
        "reworkpart_sanded_2a", validators=[DataRequired()]
    )
    reworkpart_sanded_2b = StringField(
        "reworkpart_sanded_2b", validators=[DataRequired()]
    )
    reworkpart_sanded_3a = StringField(
        "reworkpart_sanded_3a", validators=[DataRequired()]
    )
    reworkpart_sanded_3b = StringField(
        "reworkpart_sanded_3b", validators=[DataRequired()]
    )
    reworkpart_sanded_4a = StringField(
        "reworkpart_sanded_4a", validators=[DataRequired()]
    )
    reworkpart_sanded_4b = StringField(
        "reworkpart_sanded_4b", validators=[DataRequired()]
    )

    # REWORK PARTS STATUS scrap
    reworkpart_scrap_1 = StringField("reworkpart_scrap_1", validators=[DataRequired()])
    reworkpart_scrap_2a = StringField(
        "reworkpart_scrap_2a", validators=[DataRequired()]
    )
    reworkpart_scrap_2b = StringField(
        "reworkpart_scrap_2b", validators=[DataRequired()]
    )
    reworkpart_scrap_3a = StringField(
        "reworkpart_scrap_3a", validators=[DataRequired()]
    )
    reworkpart_scrap_3b = StringField(
        "reworkpart_scrap_3b", validators=[DataRequired()]
    )
    reworkpart_scrap_4a = StringField(
        "reworkpart_scrap_4a", validators=[DataRequired()]
    )
    reworkpart_scrap_4b = StringField(
        "reworkpart_scrap_4b", validators=[DataRequired()]
    )
    reworkpart_scrap_2c = StringField(
        "reworkpart_scrap_2c", validators=[DataRequired()]
    )

    # customer complaints plan
    customercomplaints_plan_1 = StringField(
        "customercomplaints_plan_1", validators=[DataRequired()]
    )
    customercomplaints_plan_2 = StringField(
        "customercomplaints_plan_2", validators=[DataRequired()]
    )
    customercomplaints_plan_3 = StringField(
        "customercomplaints_plan_3", validators=[DataRequired()]
    )

    # customer complaints actual
    customercomplaints_actual_1 = StringField(
        "customercomplaints_actual_1", validators=[DataRequired()]
    )
    customercomplaints_actual_2 = StringField(
        "customercomplaints_actual_2", validators=[DataRequired()]
    )
    customercomplaints_actual_3 = StringField(
        "customercomplaints_actual_3", validators=[DataRequired()]
    )

    # customer complaints top 3 reasons
    customercomplaints_top3reasons_1a = StringField(
        "customercomplaints_top3reasons_1a", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_1b = StringField(
        "customercomplaints_top3reasons_1b", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_1c = StringField(
        "customercomplaints_top3reasons_1c", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_2a = StringField(
        "customercomplaints_top3reasons_2a", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_2b = StringField(
        "customercomplaints_top3reasons_2b", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_2c = StringField(
        "customercomplaints_top3reasons_2c", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_3a = StringField(
        "customercomplaints_top3reasons_3a", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_3b = StringField(
        "customercomplaints_top3reasons_3b", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_3c = StringField(
        "customercomplaints_top3reasons_3c", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_4a = StringField(
        "customercomplaints_top3reasons_4a", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_4b = StringField(
        "customercomplaints_top3reasons_4b", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_4c = StringField(
        "customercomplaints_top3reasons_4c", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_5a = StringField(
        "customercomplaints_top3reasons_5a", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_5b = StringField(
        "customercomplaints_top3reasons_5b", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_5c = StringField(
        "customercomplaints_top3reasons_5c", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_6a = StringField(
        "customercomplaints_top3reasons_6a", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_6b = StringField(
        "customercomplaints_top3reasons_6b", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_6c = StringField(
        "customercomplaints_top3reasons_6c", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_7a = StringField(
        "customercomplaints_top3reasons_7a", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_7b = StringField(
        "customercomplaints_top3reasons_7b", validators=[DataRequired()]
    )
    customercomplaints_top3reasons_7c = StringField(
        "customercomplaints_top3reasons_7c", validators=[DataRequired()]
    )

    # customer complaints action
    customercomplaints_action_1a = StringField(
        "customercomplaints_action_1a", validators=[DataRequired()]
    )
    customercomplaints_action_1b = StringField(
        "customercomplaints_action_1b", validators=[DataRequired()]
    )
    customercomplaints_action_1c = StringField(
        "customercomplaints_action_1c", validators=[DataRequired()]
    )
    customercomplaints_action_2a = StringField(
        "customercomplaints_action_2a", validators=[DataRequired()]
    )
    customercomplaints_action_2b = StringField(
        "customercomplaints_action_2b", validators=[DataRequired()]
    )
    customercomplaints_action_2c = StringField(
        "customercomplaints_action_2c", validators=[DataRequired()]
    )
    customercomplaints_action_3a = StringField(
        "customercomplaints_action_3a", validators=[DataRequired()]
    )
    customercomplaints_action_3b = StringField(
        "customercomplaints_action_3b", validators=[DataRequired()]
    )
    customercomplaints_action_3c = StringField(
        "customercomplaints_action_3c", validators=[DataRequired()]
    )
    customercomplaints_action_4a = StringField(
        "customercomplaints_action_4a", validators=[DataRequired()]
    )
    customercomplaints_action_4b = StringField(
        "customercomplaints_action_4b", validators=[DataRequired()]
    )
    customercomplaints_action_4c = StringField(
        "customercomplaints_action_4c", validators=[DataRequired()]
    )
    customercomplaints_action_5a = StringField(
        "customercomplaints_action_5a", validators=[DataRequired()]
    )
    customercomplaints_action_5b = StringField(
        "customercomplaints_action_5b", validators=[DataRequired()]
    )
    customercomplaints_action_5c = StringField(
        "customercomplaints_action_5c", validators=[DataRequired()]
    )
    customercomplaints_action_6a = StringField(
        "customercomplaints_action_6a", validators=[DataRequired()]
    )
    customercomplaints_action_6b = StringField(
        "customercomplaints_action_6b", validators=[DataRequired()]
    )
    customercomplaints_action_6c = StringField(
        "customercomplaints_action_6c", validators=[DataRequired()]
    )
    customercomplaints_action_7a = StringField(
        "customercomplaints_action_7a", validators=[DataRequired()]
    )
    customercomplaints_action_7b = StringField(
        "customercomplaints_action_7b", validators=[DataRequired()]
    )
    customercomplaints_action_7c = StringField(
        "customercomplaints_action_7c", validators=[DataRequired()]
    )


class Form3Form(Form):
    # actual
    actual_1 = StringField("actual_1", validators=[DataRequired()])
    actual_2 = StringField("actual_2", validators=[DataRequired()])
    actual_3 = StringField("actual_3", validators=[DataRequired()])
    actual_4 = StringField("actual_4", validators=[DataRequired()])
    actual_5 = StringField("actual_5", validators=[DataRequired()])
    actual_6 = StringField("actual_6", validators=[DataRequired()])
    actual_7 = StringField("actual_7", validators=[DataRequired()])
    actual_8 = StringField("actual_8", validators=[DataRequired()])
    actual_total = StringField("actual_totala", validators=[DataRequired()])

    # customercomplaint_1a
    customercomplaint_1a = StringField(
        "customercomplaint_1a", validators=[DataRequired()]
    )
    customercomplaint_2a = StringField(
        "customercomplaint_2a", validators=[DataRequired()]
    )
    customercomplaint_3a = StringField(
        "customercomplaint_3a", validators=[DataRequired()]
    )
    customercomplaint_4a = StringField(
        "customercomplaint_4a", validators=[DataRequired()]
    )
    customercomplaint_5a = StringField(
        "customercomplaint_5a", validators=[DataRequired()]
    )
    customercomplaint_6a = StringField(
        "customercomplaint_6a", validators=[DataRequired()]
    )
    customercomplaint_7a = StringField(
        "customercomplaint_7a", validators=[DataRequired()]
    )
    customercomplaint_8a = StringField(
        "customercomplaint_8a", validators=[DataRequired()]
    )
    customercomplaint_totala = StringField(
        "customercomplaint_totala", validators=[DataRequired()]
    )

    # sd
    sd_1 = StringField("sd_1", validators=[DataRequired()])
    sd_2 = StringField("sd_2", validators=[DataRequired()])
    sd_3 = StringField("sd_3", validators=[DataRequired()])
    sd_4 = StringField("sd_4", validators=[DataRequired()])
    sd_5 = StringField("sd_5", validators=[DataRequired()])
    sd_6 = StringField("sd_6", validators=[DataRequired()])
    sd_7 = StringField("sd_7", validators=[DataRequired()])
    sd_8 = StringField("sd_8", validators=[DataRequired()])
    sd_total = StringField("sd_total", validators=[DataRequired()])

    # RD
    rd_1 = StringField("rd_1", validators=[DataRequired()])
    rd_2 = StringField("rd_2", validators=[DataRequired()])
    rd_3 = StringField("rd_3", validators=[DataRequired()])
    rd_4 = StringField("rd_4", validators=[DataRequired()])
    rd_5 = StringField("rd_5", validators=[DataRequired()])
    rd_6 = StringField("rd_6", validators=[DataRequired()])
    rd_7 = StringField("rd_7", validators=[DataRequired()])
    rd_8 = StringField("rd_8", validators=[DataRequired()])
    rd_total = StringField("rd_total", validators=[DataRequired()])

    # customercomplaint_1b
    customercomplaint_1b = StringField(
        "customercomplaint_1b", validators=[DataRequired()]
    )
    customercomplaint_2b = StringField(
        "customercomplaint_2b", validators=[DataRequired()]
    )
    customercomplaint_3b = StringField(
        "customercomplaint_3b", validators=[DataRequired()]
    )
    customercomplaint_4b = StringField(
        "customercomplaint_4b", validators=[DataRequired()]
    )
    customercomplaint_5b = StringField(
        "customercomplaint_5b", validators=[DataRequired()]
    )
    customercomplaint_6b = StringField(
        "customercomplaint_6b", validators=[DataRequired()]
    )
    customercomplaint_7b = StringField(
        "customercomplaint_7b", validators=[DataRequired()]
    )
    customercomplaint_8b = StringField(
        "customercomplaint_8b", validators=[DataRequired()]
    )
    customercomplaint_totalb = StringField(
        "customercomplaint_totalb", validators=[DataRequired()]
    )

    # top 3 reasons
    t3r_1 = StringField("top3r_1", validators=[DataRequired()])
    t3r_2 = StringField("top3r_2", validators=[DataRequired()])
    t3r_3 = StringField("top3r_3", validators=[DataRequired()])
    t3r_4 = StringField("top3r_4", validators=[DataRequired()])
    t3r_5 = StringField("top3r_5", validators=[DataRequired()])
    t3r_6 = StringField("top3r_6", validators=[DataRequired()])
    t3r_7 = StringField("top3r_7", validators=[DataRequired()])
    t3r_8 = StringField("top3r_8", validators=[DataRequired()])
    t3r_total = StringField("top3r_total", validators=[DataRequired()])

    # dust
    dust_1 = StringField("dust_1", validators=[DataRequired()])
    dust_2 = StringField("dust_2", validators=[DataRequired()])
    dust_3 = StringField("dust_3", validators=[DataRequired()])
    dust_4 = StringField("dust_4", validators=[DataRequired()])
    dust_5 = StringField("dust_5", validators=[DataRequired()])
    dust_6 = StringField("dust_6", validators=[DataRequired()])
    dust_7 = StringField("dust_7", validators=[DataRequired()])
    dust_8 = StringField("dust_8", validators=[DataRequired()])
    dust_total = StringField("dust_total", validators=[DataRequired()])

    # UC
    uc_1 = StringField("uc_1", validators=[DataRequired()])
    uc_2 = StringField("uc_2", validators=[DataRequired()])
    uc_3 = StringField("uc_3", validators=[DataRequired()])
    uc_4 = StringField("uc_4", validators=[DataRequired()])
    uc_5 = StringField("uc_5", validators=[DataRequired()])
    uc_6 = StringField("uc_6", validators=[DataRequired()])
    uc_7 = StringField("uc_7", validators=[DataRequired()])
    uc_8 = StringField("uc_8", validators=[DataRequired()])
    uc_total = StringField("uc_total", validators=[DataRequired()])

    # DS
    ds_1 = StringField("ds_1", validators=[DataRequired()])
    ds_2 = StringField("ds_2", validators=[DataRequired()])
    ds_3 = StringField("ds_3", validators=[DataRequired()])
    ds_4 = StringField("ds_4", validators=[DataRequired()])
    ds_5 = StringField("ds_5", validators=[DataRequired()])
    ds_6 = StringField("ds_6", validators=[DataRequired()])
    ds_7 = StringField("ds_7", validators=[DataRequired()])
    ds_8 = StringField("ds_8", validators=[DataRequired()])
    ds_total = StringField("ds_total", validators=[DataRequired()])

    # SPITT
    spitt_1 = StringField("spitt_1", validators=[DataRequired()])
    spitt_2 = StringField("spitt_2", validators=[DataRequired()])
    spitt_3 = StringField("spitt_3", validators=[DataRequired()])
    spitt_4 = StringField("spitt_4", validators=[DataRequired()])
    spitt_5 = StringField("spitt_5", validators=[DataRequired()])
    spitt_6 = StringField("spitt_6", validators=[DataRequired()])
    spitt_7 = StringField("spitt_7", validators=[DataRequired()])
    spitt_8 = StringField("spitt_8", validators=[DataRequired()])
    spitt_total = StringField("spitt_total", validators=[DataRequired()])
    # OThers
    others_1 = StringField("others_1", validators=[DataRequired()])
    others_2 = StringField("others_2", validators=[DataRequired()])
    others_3 = StringField("others_3", validators=[DataRequired()])
    others_4 = StringField("others_4", validators=[DataRequired()])
    others_5 = StringField("others_5", validators=[DataRequired()])
    others_6 = StringField("others_6", validators=[DataRequired()])
    others_7 = StringField("others_7", validators=[DataRequired()])
    others_8 = StringField("others_8", validators=[DataRequired()])
    others_total = StringField("others_total", validators=[DataRequired()])

    reg = StringField("reg", validators=[DataRequired()])
    cl = StringField("cl", validators=[DataRequired()])
    plan = StringField("plan", validators=[DataRequired()])
    faid = StringField("faid", validators=[DataRequired()])
    nmiss = StringField("nmiss", validators=[DataRequired()])

    breakdowndetails = StringField("breakdowndetails", validators=[DataRequired()])
    shortcommunication = StringField(
        "shortagecommunication", validators=[DataRequired()]
    )
    feedback = StringField("feedback", validators=[DataRequired()])
    teamleadersign = StringField("teamleadersign", validators=[DataRequired()])
    groupleadersign = StringField("groupleadersign", validators=[DataRequired()])

    # standupmeetings
    standup_p = StringField("standup_p", validators=[DataRequired()])
    standup_q = StringField("standup_q", validators=[DataRequired()])
    standup_c = StringField("standup_c", validators=[DataRequired()])
    standup_d = StringField("standup_d", validators=[DataRequired()])
    standup_m = StringField("standup_m", validators=[DataRequired()])
    standup_s = StringField("standup_s", validators=[DataRequired()])
