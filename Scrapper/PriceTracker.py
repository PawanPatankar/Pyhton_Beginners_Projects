import requests
from bs4 import BeautifulSoup
from json import dump, loads
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


guitar=input("Enter Model Name")
# c=a.split(' ')
# print(c)
# for i in c:
output=''
for i in guitar:
    if i==' ':
        output+='+'
    else:
     output+=i

musicstore=output
snapdeal=output
raj=output
bajao=output
flipkart=output
furtados=output
shopclues=output
euphonycart=output
acousticbits=output
output+='+amazon'
musicstore+='+musicstore'
snapdeal+='+snapdeal'
furtados+='+furtadosonline'
shopclues+='+shopclues'
euphonycart+='+euphonycart'
acousticbits+='+acousticbits'

bajao+='+bajaao'
flipkart+='+flipkart'
raj+='+raj+musical'



try:
    url=f'https://www.google.com/search?source=hp&ei=9HRJXZLTGYf1rQHt-IaIDw&q={output}&oq={output}&gs_l=psy-ab.3..35i39j0j0i10l8.1682.3739..4150...1.0..0.342.1851.0j7j1j1......0....1..gws-wiz.....6..0i131j0i67j0i20i263.Y2Nhmop6tes&ved=0ahUKEwiSndrmoe7jAhWHeisKHW28AfEQ4dUDCAU&uact=5'
    url2=f'https://www.google.com/search?source=hp&ei=9HRJXZLTGYf1rQHt-IaIDw&q={bajao}&oq={bajao}&gs_l=psy-ab.3..35i39j0j0i10l8.1682.3739..4150...1.0..0.342.1851.0j7j1j1......0....1..gws-wiz.....6..0i131j0i67j0i20i263.Y2Nhmop6tes&ved=0ahUKEwiSndrmoe7jAhWHeisKHW28AfEQ4dUDCAU&uact=5'
    url3=f'https://www.google.com/search?source=hp&ei=9HRJXZLTGYf1rQHt-IaIDw&q={flipkart}&oq={flipkart}&gs_l=psy-ab.3..35i39j0j0i10l8.1682.3739..4150...1.0..0.342.1851.0j7j1j1......0....1..gws-wiz.....6..0i131j0i67j0i20i263.Y2Nhmop6tes&ved=0ahUKEwiSndrmoe7jAhWHeisKHW28AfEQ4dUDCAU&uact=5'
    url4=f'https://www.google.com/search?source=hp&ei=9HRJXZLTGYf1rQHt-IaIDw&q={raj}&oq={raj}&gs_l=psy-ab.3..35i39j0j0i10l8.1682.3739..4150...1.0..0.342.1851.0j7j1j1......0....1..gws-wiz.....6..0i131j0i67j0i20i263.Y2Nhmop6tes&ved=0ahUKEwiSndrmoe7jAhWHeisKHW28AfEQ4dUDCAU&uact=5'
    url5=f'https://www.google.com/search?source=hp&ei=9HRJXZLTGYf1rQHt-IaIDw&q={musicstore}&oq={musicstore}&gs_l=psy-ab.3..35i39j0j0i10l8.1682.3739..4150...1.0..0.342.1851.0j7j1j1......0....1..gws-wiz.....6..0i131j0i67j0i20i263.Y2Nhmop6tes&ved=0ahUKEwiSndrmoe7jAhWHeisKHW28AfEQ4dUDCAU&uact=5'
    url6=f'https://www.google.com/search?source=hp&ei=9HRJXZLTGYf1rQHt-IaIDw&q={snapdeal}&oq={snapdeal}&gs_l=psy-ab.3..35i39j0j0i10l8.1682.3739..4150...1.0..0.342.1851.0j7j1j1......0....1..gws-wiz.....6..0i131j0i67j0i20i263.Y2Nhmop6tes&ved=0ahUKEwiSndrmoe7jAhWHeisKHW28AfEQ4dUDCAU&uact=5'
    url7=f'https://www.google.com/search?source=hp&ei=9HRJXZLTGYf1rQHt-IaIDw&q={furtados}&oq={furtados}&gs_l=psy-ab.3..35i39j0j0i10l8.1682.3739..4150...1.0..0.342.1851.0j7j1j1......0....1..gws-wiz.....6..0i131j0i67j0i20i263.Y2Nhmop6tes&ved=0ahUKEwiSndrmoe7jAhWHeisKHW28AfEQ4dUDCAU&uact=5'
    url8=f'https://www.google.com/search?source=hp&ei=9HRJXZLTGYf1rQHt-IaIDw&q={shopclues}&oq={shopclues}&gs_l=psy-ab.3..35i39j0j0i10l8.1682.3739..4150...1.0..0.342.1851.0j7j1j1......0....1..gws-wiz.....6..0i131j0i67j0i20i263.Y2Nhmop6tes&ved=0ahUKEwiSndrmoe7jAhWHeisKHW28AfEQ4dUDCAU&uact=5'
    url9=f'https://www.google.com/search?source=hp&ei=9HRJXZLTGYf1rQHt-IaIDw&q={euphonycart}&oq={euphonycart}&gs_l=psy-ab.3..35i39j0j0i10l8.1682.3739..4150...1.0..0.342.1851.0j7j1j1......0....1..gws-wiz.....6..0i131j0i67j0i20i263.Y2Nhmop6tes&ved=0ahUKEwiSndrmoe7jAhWHeisKHW28AfEQ4dUDCAU&uact=5'
    url10=f'https://www.google.com/search?source=hp&ei=9HRJXZLTGYf1rQHt-IaIDw&q={acousticbits}&oq={acousticbits}&gs_l=psy-ab.3..35i39j0j0i10l8.1682.3739..4150...1.0..0.342.1851.0j7j1j1......0....1..gws-wiz.....6..0i131j0i67j0i20i263.Y2Nhmop6tes&ved=0ahUKEwiSndrmoe7jAhWHeisKHW28AfEQ4dUDCAU&uact=5'
    # print(serches)

    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    #
    responseg2 = requests.get(url,headers=headers, verify=False, timeout=30).text
    soup = BeautifulSoup(responseg2, 'lxml')
    data = soup.find_all('div', class_="r")
    links = []
    for i in data:
            link = i.find('a', href=True)
            link = link['href']
            links.append(link)
            break
    # print(links)
    ids = ''
    for i in links:
            a = i.split('/')
            a = a[5]
            ids+=a
    # print(ids)


    responseg3 = requests.get(url2,headers=headers, verify=False, timeout=30).text
    soup = BeautifulSoup(responseg3, 'lxml')
    data = soup.find_all('div', class_="r")
    linksbajao =''


    for i in data:
            link = i.find('a', href=True)
            link = link['href']
            linksbajao+=link
            break
    # print(linksbajao)

    priceamazon=''
    priceamazon2=''
    priceamazondeal=''
    pricebajao=''
    priceraj=''
    pricemusicstore=''
    pricesnapdeal=''
    pricefurtados=''
    priceshopclues=''
    priceephony=''
    priceaccostic=''


    priceoth2=[]
    conditionoth2=[]
    selleroth2=[]
    nameamazon=''
    namebajao=''
    rajname=''
    namefipkart=''
    msname=''
    namesnapdeal=''
    namefurtados=''
    nameshopclues=''
    nameephony=''
    nameaccostic=''

    amazonallprice=f'https://www.amazon.in/gp/offer-listing/{ids}'

    responseg3 = requests.get(amazonallprice, headers=headers, verify=False, timeout=30).text
            # print(responseg2)
    soup2 = BeautifulSoup(responseg3, 'lxml')
    # for j in soup2.find_all('h3',attrs={'class':'a-spacing-none olpSellerName'}):
    #     print(j.span.text)
    for i in soup2.find_all('div',attrs={'class':'a-section a-spacing-double-large'}):
                for price1 in i.findAll('div', attrs={'class': 'a-row a-spacing-mini olpOffer'}):
                    # print(price1)
                    for price,condition in zip(price1.find_all('span',attrs={'class':'a-size-large a-color-price olpOfferPrice a-text-bold'}),price1.findAll('span', attrs={'class': 'a-size-medium olpCondition a-text-bold'})):
                        priceoth=price.span.text.replace('\xa0\xa0','')
                        conditionoth=condition.text.replace('\n','')
                        conditionoth=conditionoth.replace(' ','')

                        priceoth2.append(priceoth)
                        conditionoth2.append(conditionoth)
    for j in soup2.find_all('h3',attrs={'class':'a-spacing-none olpSellerName'}):
        selleroth=j.span.text
        selleroth2.append(selleroth)

    for z in soup2.find_all('div',attrs={'id':'olpProductDetails'}):
        name=z.h1.text
        nameamazon+=name

    responseg4 = requests.get(linksbajao, headers=headers, verify=False, timeout=30).text
            # print(responseg2)
    soup3 = BeautifulSoup(responseg4, 'lxml')
    for i in soup3.find_all('div',attrs={'class':'price--main'}):
                for price1 in i.findAll('span', attrs={'class': 'money'}):
                    price3=price1.text.replace(' ','')
                    price4 = price3.replace('\n', '')

                    # print(price3)
                    pricebajao+=price4
    for k in soup3.find_all('div',attrs={'class':'product-details'}):
        namebaj=k.h1.text
        namebajao+=namebaj



    responseg5 = requests.get(url3,headers=headers, verify=False, timeout=30).text
    soup = BeautifulSoup(responseg5, 'lxml')
    data = soup.find_all('div', class_="r")
    links = []
    for i in data:
            link = i.find('a', href=True)
            link = link['href']
            links.append(link)
            break
    # print(links)
    idsflipkart = ''
    for i in links:
            a = i.split('/')
            a = a[5]
            idsflipkart+=a


    flipprice=''
    flipurl=f'http://www.flipkart.com/sadsad/p/{idsflipkart}'
    # print(flipurl)
    responseg7 = requests.get(flipurl, headers=headers, verify=False, timeout=30).text

    soup6 = BeautifulSoup(responseg7, 'lxml')

    for i in soup6.find_all('div',attrs={'class':'_1vC4OE _3qQ9m1'}):
        priceflip=i.text
        # print("price",priceflip)
        flipprice+=priceflip
    for m in soup6.find_all('span',attrs={'class':'_35KyD6'}):
        nameflip=m.text
        # print("price",priceflip)
        namefipkart+=nameflip


    responseg0 = requests.get(url4,headers=headers, verify=False, timeout=30).text
    soup0 = BeautifulSoup(responseg0, 'lxml')
    data = soup0.find_all('div', class_="r")
    linksraj =''
    for i in data:
            link = i.find('a', href=True)
            link = link['href']
            linksraj+=link
            break
    responseg8 = requests.get(linksraj, headers=headers, verify=False, timeout=30).text
            # print(responseg2)
    soup8 = BeautifulSoup(responseg8, 'lxml')
    for i in soup8.find_all('span',attrs={'id':'our_price_display'}):
                    price35=i.text
                    price45 = price35
                    priceraj+=price45

    for s in soup8.find_all('div',attrs={'id':'product_name_wrap'}):
                    rajnam=s.h1.text
                    rajname+=rajnam

    #-------------------------------------------MUSIC STORE---------------------------

    responseg12 = requests.get(url5,headers=headers, verify=False, timeout=30).text
    soup01 = BeautifulSoup(responseg12, 'lxml')
    data1 = soup01.find_all('div', class_="r")
    linksmusicstore =''
    for i in data1:
            link = i.find('a', href=True)
            link = link['href']
            linksmusicstore+=link
            break
    responseg13 = requests.get(linksmusicstore, headers=headers, verify=False, timeout=30).text
            # print(responseg2)
    soup21 = BeautifulSoup(responseg13, 'lxml')
    for i in soup21.find_all('div',attrs={'class':'current-price'}):
                    pricems=i.span.text
                    pricems = pricems
                    pricemusicstore+=pricems

    for s in soup21.find_all('h1',attrs={'itemprop':'name'}):
                    msnam=s.text
                    msname+=msnam

    #-------------------------------------------SNAPDEAL---------------------------

    responseg12 = requests.get(url6,headers=headers, verify=False, timeout=30).text
    soup01 = BeautifulSoup(responseg12, 'lxml')
    data1 = soup01.find_all('div', class_="r")
    linksnapdeal =''
    for i in data1:
            link = i.find('a', href=True)
            link = link['href']
            linksnapdeal+=link
            break
    responseg13 = requests.get(linksnapdeal, headers=headers, verify=False, timeout=30).text
            # print(responseg2)
    soup21 = BeautifulSoup(responseg13, 'lxml')
    for i in soup21.find_all('span',attrs={'class':'payBlkBig'}):
                    pricems=i.text
                    pricems = pricems
                    pricesnapdeal+=pricems

    for s in soup21.find_all('h1',attrs={'itemprop':'name'}):
                    namesd=s.text
                    namesnapdeal+=namesd


    #-------------------------------------------FURTADOSONLINE---------------------------

    responseg12 = requests.get(url7,headers=headers, verify=False, timeout=30).text
    soup01 = BeautifulSoup(responseg12, 'lxml')
    data1 = soup01.find_all('div', class_="r")
    linkfurtados =''
    for i in data1:
            link = i.find('a', href=True)
            link = link['href']
            linkfurtados+=link
            break
    responseg13 = requests.get(linkfurtados, headers=headers, verify=False, timeout=30).text
            # print(responseg2)
    soup21 = BeautifulSoup(responseg13, 'lxml')
    for i in soup21.find_all('div',attrs={'class':'price-box'}):
                    pricems=i.span.text
                    pricems = pricems
                    pricefurtados+=pricems

    for s in soup21.find_all('h1',attrs={'class':'name'}):
                    namesd=s.text
                    namefurtados+=namesd

    #-------------------------------------------SHOPCLUES---------------------------

    responseg12 = requests.get(url8,headers=headers, verify=False, timeout=30).text
    soup01 = BeautifulSoup(responseg12, 'lxml')
    data1 = soup01.find_all('div', class_="r")
    linkshopclues =''
    for i in data1:
            link = i.find('a', href=True)
            link = link['href']
            linkshopclues+=link
            break
    responseg13 = requests.get(linkshopclues, headers=headers, verify=False, timeout=30).text
            # print(responseg2)
    soup21 = BeautifulSoup(responseg13, 'lxml')
    for i in soup21.find_all('span',attrs={'class':'f_price'}):
                    pricems=i.text
                    pricems = pricems
                    priceshopclues+=pricems

    for s in soup21.find_all('h1',attrs={'itemprop':'name'}):
                    namesd=s.text
                    nameshopclues+=namesd

    #-------------------------------------------ephuonycart---------------------------

    responseg12 = requests.get(url9,headers=headers, verify=False, timeout=30).text
    soup01 = BeautifulSoup(responseg12, 'lxml')
    data1 = soup01.find_all('div', class_="r")
    linkephony =''
    for i in data1:
            link = i.find('a', href=True)
            link = link['href']
            linkephony+=link
            break
    responseg13 = requests.get(linkephony, headers=headers, verify=False, timeout=30).text
            # print(responseg2)
    soup21 = BeautifulSoup(responseg13, 'lxml')
    for i in soup21.find_all('p',attrs={'class':'price rtr'}):
                    pricems=i.span.text
                    pricems = pricems
                    priceephony+=pricems

    for s in soup21.find_all('h1',attrs={'class':'product_title entry-title'}):
                    namesd=s.text
                    nameephony+=namesd

    #-------------------------------------------Accosticbits---------------------------

    responseg12 = requests.get(url10,headers=headers, verify=False, timeout=30).text
    soup01 = BeautifulSoup(responseg12, 'lxml')
    data1 = soup01.find_all('div', class_="r")
    linkaccostic =''
    for i in data1:
            link = i.find('a', href=True)
            link = link['href']
            linkaccostic+=link
            break
    responseg13 = requests.get(linkaccostic, headers=headers, verify=False, timeout=30).text
            # print(responseg2)
    soup21 = BeautifulSoup(responseg13, 'lxml')
    for i in soup21.find_all('p',attrs={'class':'price'}):
                    pricems=i.span.text
                    pricems = pricems
                    priceaccostic+=pricems

    for s in soup21.find_all('h1',attrs={'class':'product_title entry-title'}):
                    namesd=s.text
                    nameaccostic+=namesd

    amazonlist=[]

    for i,j,k in zip(priceoth2,conditionoth2,selleroth2):
        amazondict = {
                        'Price': i,
                        'Condition': j,
                        'Seller': k,
                        'Name':nameamazon

                    }
        amazonlist.append(amazondict)

    bajaolist=[]
    flipkarlist=[]
    rajlist=[]
    musicstorelist=[]
    snaplist=[]
    furtadoslist=[]
    shopclueslist=[]
    ephonylist=[]
    accusticlist=[]

    bajaodict={
        'Price':pricebajao,
        'Name':namebajao
    }
    flipkartdict={
        'Price':flipprice,
        'Name':namefipkart
    }

    rajdict={
        'Price':priceraj,
        'Name':rajname
    }

    musicstoredict={
        'Price':pricemusicstore,
        'Name':msname
    }

    snapdict={
        'Price':pricesnapdeal,
        'Name':namesnapdeal
    }

    furtadosdict={
        'Price':pricefurtados,
        'Name':namefurtados
    }

    shopclusdict={
        'Price':priceshopclues,
        'Name':nameshopclues
    }
    ephonydict={
        'Price':priceephony,
        'Name':nameephony
    }

    Accosticdict={
        'Price':priceaccostic,
        'Name':nameaccostic
    }


    musicdata={
        'Amazon': amazonlist,
        'Bajaao':bajaodict,
        'Flipkart':flipkartdict,
        'RajMusical':rajdict,
        'MusicalStore':musicstoredict,
        'Snapdeal':snapdict,
        'Furtados':furtadosdict,
        'Shopclues':shopclusdict,
        'Euphonycart':ephonydict,
        'Acousticbits':Accosticdict

    }


    checkbajao=[]
    a=linksbajao.split('/')
    b=a[4]
    b=b.split('-')
    checkbajao.append(b[0])


    print("------------AMAZON PRICES---------")
    print(nameamazon)
    if len(priceoth2)==0:
        print("Product Not Available")
    else:
        print("Price             Condition    Seller")
        for i,j,k in zip(priceoth2,conditionoth2,selleroth2):
            print(f"{i}        {j}   {k}")

    print("-----------------BAJAAAO-------------")
    print(namebajao)
    checkg=guitar
    c=checkg.split()
    ch=''
    for i in c:
        ch+=i
        break
    # print(checkbajao)
    if ch in checkbajao:
        if pricebajao=='':
            print("Product Not Available")
        else:
            print("Bajaao Price",pricebajao)
    else:
        print("Not Available")


    print("-------------FLIPKART--------------------")
    print(namefipkart)
    if flipprice=='':
        print("Product Not Available")
    else:
        print(f"Flipkart Price: {flipprice}")

    print("-------------RAJ MUSICAL-------------")
    print(rajname)
    if priceraj=='':
        print("Product Not Available")
    else:
        print(f"RAJ MUSICAL: {priceraj}")

    print("-------------MUSIC STORE-------------")
    print(msname)
    if pricemusicstore=='':
        print("Product Not Available")
    else:
        print(f" MUSIC STORE: {pricemusicstore}")



    print("-------------SNAPDEAL-------------")
    print(namesnapdeal)
    if pricesnapdeal=='':
        print("Product Not Available")
    else:
        print(f" SNAPDEAL: {pricesnapdeal}")


    print("-------------FURTADOS-------------")
    print(namefurtados)
    if pricefurtados=='':
        print("Product Not Available")
    else:
        print(f" FURTADOS ONLINE: {pricefurtados}")


    print("-------------SHOPCLUES-------------")
    print(nameshopclues)
    if priceshopclues=='':
        print("Product Not Available")
    else:
        print(f" SHOPCLUES ONLINE: {priceshopclues}")


    print("-------------EPHONY-------------")
    print(nameephony)
    if priceephony=='':
        print("Product Not Available")
    else:
        print(f" EUPHONY ONLINE: {priceephony}")


    print("-------------acousticbits-------------")
    print(nameaccostic)
    if priceaccostic=='':
        print("Product Not Available")
    else:
        print(f" Acousticbits ONLINE: {priceaccostic}")


    datajsonmusic=[]
    datajsonmusic.append(musicdata)
    f = open('MUSICDATA.json', 'w')
    dump(datajsonmusic, f, indent=4)
    f.close()
except Exception:
    print("WRONG INPUT PLEASE TRY AGAIN")