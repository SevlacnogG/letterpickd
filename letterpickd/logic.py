import math
import random
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException

class control:
    opc = Options()
    opc.add_experimental_option("detach", True)
    #opc.add_argument("--headless=new") # <-- Invisible browser.
    servico = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service = servico, options = opc)
    opc.page_load_strategy = "none"
    wait = WebDriverWait(browser, 15)

    # def ciclo(self, user, decd, genr):
    #     self.acessL(user, decd, self.traGenr(genr))


    def ciclo(self, user):
        self.acessL(user)
        # ^-- Include 404 exception.
        total = self.qtdFilms()

        if total == 0:
            return 0
        else:
            pag = self.rndPag(total)

        self.acessSF(pag)

        resultado = self.pick()
        # ^-- Only verifies if the total watchlist = 0.
        # Need to update it to count if the chosen subfolder combination is 0.

        return resultado

    # def acessL(self, user, decd, genr):
    def acessL(self, user):
        subf = []

        subf.append(f"{user}/watchlist/")

        # if not user:
        #     #self.controller.acessar("films")    # <-- espera até carregar tudo, consertar
        #     subf.append("films/")
        #     if decd:
        #         subf.append(f"decade/{decd}s/")
        #     if genr:
        #         subf.append(f"genre/{genr}/")
        # else:
        #     subf.append(f"{user}/watchlist/")
        #     if decd:
        #         subf.append(f"decade/{decd}s/")
        #     if genr:
        #         subf.append(f"genre/{genr}/")

        rstd = ''.join(subf)
        # self.escolherFilme()

        self.browser.get(f"https://letterboxd.com/{rstd}")

    def acessSF(self, pag):
        url = self.browser.current_url
        # self.browser.implicitly_wait(10)
        self.browser.get(f"{url}page/{pag}")

    def traGenr(self, genr_pt):
        match genr_pt:
            case "Ação":
                return "action"
            case "Aventura":
                return "adventure"
            case "Animação":
                return "animation"
            case "Comédia":
                return "comedy"
            case "Crime":
                return "crime"
            case "Documentário":
                return "documentary"
            case "Drama":
                return "drama"
            case "Família":
                return "family"
            case "Fantasia":
                return "fantasy"
            case "Ficção Científica":
                return "science-fiction"
            case "Filme para TV":
                return "tv-movie"
            case "Guerra":
                return "war"
            case "História":
                return "history"
            case "Horror":
                return "horror"
            case "Mistério":
                return "mystery"
            case "Música":
                return "music"
            case "Romance":
                return "romance"
            case "Suspense":
                return "thriller"
            case "Velho Oeste":
                return "western"

    def qtdFilms(self):     # <-- Returns total number of watchlist movies.
                            # Need to make it only count subselections, genre(s) +- year(s).
        nums = []
        self.browser.implicitly_wait(10)
        teste = (self.browser.find_element("xpath", '//*[@id="content-nav"]/h1/span[2]')
                                            .get_attribute("innerHTML"))

        for n in teste:
            if n.isdecimal():
                nums.append(n)
            elif n != ',':
                break

        # ^-- Excludes anything but numbers and commas, which the site uses to mark thousands.
        # The loop stops after digits and commas are not read anymore to prevent
        # accidental inclusion of other content from the inner HTML, which can contain more digits.

        if nums[0] != 0:
            return int("".join(nums)) # <-- Numbers identified in the HTML as quantity.
        else:
            return 0

    def rndPag(self, qtd):
        qtdP = math.ceil(qtd / 28)
        return random.randint(1, qtdP)

    def pick(self):
        filmes = self.browser.find_elements("css selector", "li.poster-container a.frame")

        qtdFpP = len(filmes)
        filme = random.randint(0, qtdFpP - 1)

        nome = filmes[filme].get_attribute("data-original-title")
        link = filmes[filme].get_attribute("href")

        pickd = [nome, link]

        del filmes
        # filme = 1

        return pickd

    def abrir(self, url):
        webbrowser.open(url)
        self.browser.set_page_load_timeout(3)



