while True:
        
    print("bir tavşanın yakınlarındaki bir çalının arasında olduğunu fark edersin.")
    print("a) Tavşanı avlamak için çalıların arasına doğru ilerlersin.")
    print("b) Ağacın dalında oturan güvercini avlamaya karar verirsin.")
    secim1 = input("lütfen bir secenek secin 'a/b' ")

    if secim1 == "a":
        print("Tavşanın yanına yaklaşırken, onun telaşlı hareketlerini fark edersin. Hemen yayını hazırlar ve onu avlamayı başarırsın. Ateş yakarak yemeğini yaparsın ve dinlenirsin.")
        print("a) Yemek yedikten sonra, güvenli bir yere gidip uyuyabilirsin.")
        print("b) Yemek yedikten sonra, ormanda keşfe devam edersin.")
        secim12 = input("lütfen bir secenek secin 'a/b' ")
        if secim12 == "a":
            print("Güvenli bir yere gidip uyurken, yaralı bir geyik seni rahatsız eder. Onu avlamak için hazırlanırsın.")
            print("a) avlamaya calıs")
            print("b) yardım et")
            secim13 = input("lütfen bir secenek secin 'a/b' ")
            if secim13 == "a":
                print("geyikle boğuşurken boynuzu ile seni ağır yaraladı kan kaybından öldün")

        

                tekrar = input("Öldün tekrar oynamak ister misin?(E/H)\n-->")
                if tekrar.lower == "e":
                     continue
                
                    

            else:
                print("geyiğe yardım ettiğin için dostun oldu ve sana toplayıp yiyebileceğin bitkiler göstermeye başladı artık sürekli avlanmak zorunda değilsin")

        else:
            print("ormanı keşfe devam ederken karşına bi yılan çıktı ")
            print("a) saldır")
            print("b) kac")
            secim4 = input("lütfen bir secenek secin 'a/b' ")
            if secim4 == "a":
                print("yılanı öldürdün ama bu sırada sen de zehirlendin ve öldün")
                basasarma = input("oyundan cıkmak icin 'h' ye bas ")
                if basasarma == "h":
                    break 
            else:
                print("kacamadın yılan ve arkadaşları tarafından yem oldun")
                basasarma = input("oyundan cıkmak icin 'h' ye bas ")
                if basasarma == "h":
                    break 

    else:
        print("güvercini avlamak için yayını eline aldın ve güvercini vurdun")
        print("a) güvercini pişirip ye")
        print("b) daha büyük bir av için yem yap")
        secim2 = input("lütfen bir secenek secin 'a/b' ")
        if secim2 == "a":
            print("güvercin sen avlamadan önce zehirlendiği için yiyince sen de zehirlendin öldün")
            basasarma = input("oyundan cıkmak icin 'h' ye bas ")
            if basasarma == "h":
                break 
        else:
            print("ya al kendini git artık bitsin bu oyun be ")
            basasarma = input("oyundan cıkmak icin 'h' ye bas ")
            if basasarma == "h":
                break 