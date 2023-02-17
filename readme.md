# Tools used
- [Python][1] 3.11
- [Pycharm][2]
- [Google Chrome][3] Versão 110.0.5481.100 (Versão oficial) 64 bits
- [Selenium Chrome Web Driver][4] ChromeDriver 110.0.5481.77

# How to run
- Run these commands to install requests and jsonpath in a terminal with python 3.11 installed:
    - `pip install -U requests` `pip install -U jsonpath`
- To run the web automation tests you have to change the PATH variable in etapa2.py and etapa3.py to the location where the chrome webdriver is located, a chrome webdriver to Google Chrome v110 is already located within this repository
- To run etapa2.py you either open the file and run it manually with the support of an IDE tool such as VSCode, or run the command line in a terminal inside the Etapa2 folder: `.\etapa2.py`
- To run etapa3.py you either open the file and run it manually with the support of an IDE tool such as VSCode, or run the command line in a terminal inside the Etapa3 folder: `.\etapa3.py`
- To run the tests of the Etapa4 folder, you will have to use the PyCharm tool, with the tool open, go to the post request folder, and select createUser.py, run it pressing the green play button or right clicking anywhere within the code and selecting Run 'createUser', then you can select the createProdut file and to the same process. 
- You also have to change the path of createUserFileLocation, located in createUser.py and loginCredentialsFileLocation and createProductFileLocation, located in the createProduct.py
    - Remember to check in https://serverest.dev/ if the email in createUser.json is already registered, if it is, you will have to delete it manually in the delete user section.
    - Remember to run createUser first, to ensure the user is created.

[1]: https://www.python.org/
[2]: https://www.jetbrains.com/pt-br/pycharm/download/#section=windows
[3]: https://www.google.com/intl/pt-BR/chrome/
[4]: https://chromedriver.chromium.org/downloads
