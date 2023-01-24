from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StdNFTMintingPage:

    click_start_btn_xpath= "//button[contains(text(),'Start')]"
    click_connect_btn_xpath = "//button[contains(text(),'Connect')]"
    click_std_NFT_option_class= "m-auto"
    click_nft__class= "image-section"
    click_mint_btn_class= "color-white"
    click_copyright_name= "copyright"
    click_next_btn_xpath= "//button[contains(text(), 'Next')]"
    click_currency_dropdown_xpath= "//span[contains(text(),'Select')]"
    click_usd_currency_xpath = "//div[contains(text(),'USD')]"
    click_pay_btn_xpath= "//button[contains(text(),'PAY')]"
    switch_frame_xpath= "//iframe[@title='Secure payment input frame']"
    enter_card_number_ID = "Field-numberInput"
    enter_expiry_date_XPATH ="//input[@placeholder='MM / YY']"
    enter_cvc_XPATH = "//input[@placeholder='CVC']"
    click_ok_btn_XPATH ="//button[@id='okButton']"


    def __init__(self,driver):
        self.driver= driver

    def clickStartbtn(self):

        start_btn= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.click_start_btn_xpath)))
        self.driver.execute_script("arguments[0].click();", start_btn)

    def clickConnectBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.click_connect_btn_xpath))).click()

    def clickStdNFTBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, self.click_std_NFT_option_class)))

        standard_nft_btn = self.driver.find_elements(By.CLASS_NAME, self.click_std_NFT_option_class)

        self.driver.execute_script('arguments[0].click()', standard_nft_btn[0])

    def clickNFT(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, self.click_nft__class))).click()
        i=0
        image = self.driver.find_elements(By.CLASS_NAME, self.click_nft__class)
        image[i].click()

    def clickMintBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, self.click_mint_btn_class))).click()

    def clickRadioBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, self.click_copyright_name)))

        radio_btn = self.driver.find_elements(By.NAME, self.click_copyright_name)
        radio_btn[0].click()

    def clickNextBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.click_next_btn_xpath))).click()

    def clickSelectCurrency(self):

        select_dropdown= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.click_currency_dropdown_xpath)))
        self.driver.execute_script('arguments[0].click()', select_dropdown)

    def clickUSDCurrency(self):

        usd_currency= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.click_usd_currency_xpath)))
        self.driver.execute_script('arguments[0].click()', usd_currency)

    def clickPayBtn(self):

        pay_btn= WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.click_pay_btn_xpath)))
        self.driver.execute_script('arguments[0].click()', pay_btn)

    def switch_frame_stripe(self):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.switch_frame_xpath)))
        iframe_by_title = self.driver.find_element(By.XPATH, self.switch_frame_xpath)
        self.driver.switch_to.frame(iframe_by_title)

    def entercardDetails(self, cardnumber, expirydate, cvc):

        card_number = self.driver.find_element(By.ID, self.enter_card_number_ID).send_keys(cardnumber)

        expiry_date= self.driver.find_element(By.XPATH, self.enter_expiry_date_XPATH).send_keys(expirydate)

        cvc= self.driver.find_element(By.XPATH, self.enter_cvc_XPATH).send_keys(cvc)

        self.driver.switch_to.default_content()











