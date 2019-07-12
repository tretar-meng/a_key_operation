#encoding=utf-8

"""该程序为申报早间和晚间加班的代码"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

# 获取当前时间
current_time = time.strftime('%H:%M:%S:',time.localtime(time.time()))

# 询问是否调休
message = "Do you want to take day off(y/n):"
isLeisure = raw_input('\n'+message)

if current_time < '08:30:59':
    driver = webdriver.Firefox(executable_path="geckodriver.exe")
    driver.maximize_window()
    driver.get("http://10.40.40.40/OTApply/OTAgreement.aspx")
    driver.implicitly_wait(5)

    # 协议界面点击同意
    agree_button = driver.find_element_by_id("Button1").click()
    driver.implicitly_wait(5)

    # 登录加班系统
    account = driver.find_element_by_id("txtLoginID")
    account.send_keys("260295")
    password = driver.find_element_by_id("txtPassword")
    password.send_keys("mwgeqing!23")
    login_button = driver.find_element_by_id("btnLogin").click()
    driver.implicitly_wait(5)

    # 切换到左侧iframe
    driver.switch_to.frame("frmLeft")
    driver.implicitly_wait(5)

    # 点击个人加班申报
    links = driver.find_element_by_link_text("个人加班申报")
    links.click()

    # 回到主页面
    driver.switch_to.default_content()
    driver.implicitly_wait(5)

    # 切换到中间iframe
    driver.switch_to.frame("frmWorkSpace")
    driver.implicitly_wait(5)

    # 输入员工编号
    employee_id = driver.find_element_by_id("txtEmployeeNo")
    employee_id.send_keys("183027")
    driver.implicitly_wait(10)

    # 点击读取
    read_button = driver.find_element_by_id("btnGetEmpInfo").click()
    driver.implicitly_wait(5)

    # 选择科室
    offices_elements = Select(driver.find_element_by_id("ddlSubDept"))
    offices_elements.select_by_index(5)
    driver.implicitly_wait(5)

    # 选择加班类型
    type_elements = Select(driver.find_element_by_id("ddlOtType"))
    type_elements.select_by_index(1)
    driver.implicitly_wait(5)

    # 选择加班性质
    property_elements = Select(driver.find_element_by_id("ddlOTProperty"))
    property_elements.select_by_index(3)
    driver.implicitly_wait(5)

    # 选择上班类别【特殊排班】
    DutyType_elements = Select(driver.find_element_by_id("ddlOTDutyType"))
    DutyType_elements.select_by_index(4)
    driver.implicitly_wait(5)

    # 不调休执则行此处代码
    if isLeisure == 'n':
        DayOff_elements = Select(driver.find_element_by_id("iptIsEHoliday"))
        DayOff_elements.select_by_index(1)

    # 填写加班内容
    overtime_content = driver.find_element_by_id("txtOtContent")
    overtime_content.send_keys(u"跟进项目")
    driver.implicitly_wait(10)

    # 选择加班开始时间
    starttime_elements = Select(driver.find_element_by_id("iptStartTime"))
    if current_time < '08:00:00':
        starttime_elements.select_by_index(32)
    else:
        starttime_elements.select_by_index(33)

    # 选择加班结束时间
    endtime_elements = Select(driver.find_element_by_id("iptEndTime"))
    endtime_elements.select_by_index(34)
    driver.implicitly_wait(5)

    # 填写时间证实人
    prove_person = driver.find_element_by_id("txtTimeProvePerson")
    prove_person.send_keys(u"李雪蒙")
    driver.implicitly_wait(10)

    # 选择科室审批人
    off_prover_elements = Select(driver.find_element_by_id("iptCensorL2"))
    off_prover_elements.select_by_index(12)
    driver.implicitly_wait(5)

    # 选择部门审批人
    dep_prover_elements = Select(driver.find_element_by_id("ddlDeptApprovePerson"))
    dep_prover_elements.select_by_index(1)
    driver.implicitly_wait(5)

    # 点击提交
    submit_button = driver.find_element_by_id("btnSave").click()
    time.sleep(2)

    # 控制台打印结果
    print("\nSuccessfully!")

    if current_time > '08:00:00':
        try:
            ActionChains(driver).send_keys(Keys.ENTER).perform()
        except UnexpectedAlertPresentException:
            # 回到主页面
            driver.switch_to.default_content()
            driver.implicitly_wait(5)

            # 切换到左侧iframe
            driver.switch_to.frame("frmLeft")
            driver.implicitly_wait(5)

            # 点击个人加班修改/查询
            links = driver.find_element_by_link_text("个人加班修改/查询")
            links.click()

            # 回到主页面
            driver.switch_to.default_content()
            driver.implicitly_wait(5)

            # 切换到中间iframe
            driver.switch_to.frame("frmWorkSpace")
            driver.implicitly_wait(5)

            # 点击第一条记录的修改
            edit_button = driver.find_element_by_id("GridView1_ctl03_lbtEdit")
            edit_button.click()
            driver.implicitly_wait(5)

            # 修改加班开始时间
            edit_start_time = Select(driver.find_element_by_id("iptStartTime"))
            edit_start_time.select_by_index(32)
            driver.implicitly_wait(5)

            # 点击修改/保存按钮
            save_button = driver.find_element_by_id("btnSave")
            save_button.click()

            # 控制台打印结果
            print("\nSuccessfully!")

else:
    index1 = "74---18:30    76---19:00    78---19:30"
    index2 = "80---20:00    82---20:30    84---21:00"
    print("\n---------------------------------------")
    print('\n'+index1)
    print(index2)
    endtime_index = input("\nPlease input the index of end-time:")

    # 驱动火狐浏览器登录加班系统
    driver = webdriver.Firefox(executable_path="geckodriver.exe")
    driver.maximize_window()
    driver.get("http://10.40.40.40/OTApply/OTAgreement.aspx")
    driver.implicitly_wait(5)

    # 协议界面点击同意
    agree_button = driver.find_element_by_id("Button1").click()
    driver.implicitly_wait(5)

    # 登录加班系统
    account = driver.find_element_by_id("txtLoginID")
    account.send_keys("260295")
    password = driver.find_element_by_id("txtPassword")
    password.send_keys("mwgeqing!23")
    login_button = driver.find_element_by_id("btnLogin").click()
    driver.implicitly_wait(5)

    # 切换到左侧iframe
    driver.switch_to.frame("frmLeft")
    driver.implicitly_wait(5)

    # 点击个人加班申报
    links = driver.find_element_by_link_text("个人加班申报")
    links.click()

    # 回到主页面
    driver.switch_to.default_content()
    driver.implicitly_wait(5)

    # 切换到中间iframe
    driver.switch_to.frame("frmWorkSpace")
    driver.implicitly_wait(5)

    # 输入员工编号
    employee_id = driver.find_element_by_id("txtEmployeeNo")
    employee_id.send_keys("183027")
    driver.implicitly_wait(10)

    # 点击读取
    read_button = driver.find_element_by_id("btnGetEmpInfo").click()
    driver.implicitly_wait(5)

    # 选择科室
    offices_elements = Select(driver.find_element_by_id("ddlSubDept"))
    offices_elements.select_by_index(5)
    driver.implicitly_wait(5)

    # 选择加班类型
    type_elements = Select(driver.find_element_by_id("ddlOtType"))
    type_elements.select_by_index(1)
    driver.implicitly_wait(5)

    # 选择加班性质
    property_elements = Select(driver.find_element_by_id("ddlOTProperty"))
    property_elements.select_by_index(3)
    driver.implicitly_wait(5)

    # 选择上班类别【白班】
    DutyType_elements = Select(driver.find_element_by_id("ddlOTDutyType"))
    DutyType_elements.select_by_index(1)
    driver.implicitly_wait(5)

    # 不调休执则行此处代码
    if isLeisure == 'n':
        DayOff_elements = Select(driver.find_element_by_id("iptIsEHoliday"))
        DayOff_elements.select_by_index(1)

    # 填写加班内容
    overtime_content = driver.find_element_by_id("txtOtContent")
    overtime_content.send_keys(u"跟进项目")
    driver.implicitly_wait(10)

    # 选择加班结束时间
    endtime_elements = Select(driver.find_element_by_id("iptEndTime"))
    endtime_elements.select_by_index(endtime_index)
    driver.implicitly_wait(5)

    # 填写时间证实人
    prove_person = driver.find_element_by_id("txtTimeProvePerson")
    prove_person.send_keys(u"李雪蒙")
    driver.implicitly_wait(10)

    # 选择科室审批人
    off_prover_elements = Select(driver.find_element_by_id("iptCensorL2"))
    off_prover_elements.select_by_index(12)
    driver.implicitly_wait(5)

    # 选择部门审批人
    dep_prover_elements = Select(driver.find_element_by_id("ddlDeptApprovePerson"))
    dep_prover_elements.select_by_index(1)
    driver.implicitly_wait(5)

    # 点击提交
    submit_button = driver.find_element_by_id("btnSave").click()

    # 控制台打印结果
    print("\nSuccessfully!")