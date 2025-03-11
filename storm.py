import streamlit as st
from random import *
from statistics import *

st.title("Kugle kugler online 1.0")
st.write("Denne webappen er basert på Kugle-1-2-3, som forklart i boka Stokastik. Programmet var ikkje å finne lenger, så eg laga ein web-versjon av det.")

def gjennomsnitt(lst):
  return mean(lst)

def typetal(lst):
  return mode(lst)

def varians(lst):
  return(variance(lst))

def skriv_regnskap(lst, modell,numsim):
  st.divider()
  if len(lst)<250:
    st.text("Liste over resultat: ")
    st.text(lst)
  st.write("Typetal: ", typetal(lst))
  st.write(f"Gjennomsnittet: {gjennomsnitt(lst): .2f}")
  if numsim>1:
    var=variance(lst)
    std=var**0.5
    st.write(f"Varians: {var: .2f}")
    st.write(f"Standardavvik: {std: .2f}")
  st.text("")
  if modell==1:
    if antall_som_trekkes<50: #Skriver ut kor mange gonger dei forskjellige verdiane dukket opp, dersom det er mindre enn 50 kuler
     for k in range(antall_som_trekkes+1):
       st.write("Antal gongar du trekte ", k, "raude : ", sum(1 for i in lst if i  == k),"  ")
  st.write(":sunglasses:")

def trekk(antall=1):
  global raude
  global kvite
  global resultatstreng
  if tilbakelegging==True:
    for i in range(antall):
      kulenr=randint(1,len(eske))
      if eske[kulenr-1]==1:
        raude = raude+1
        resultatstreng=resultatstreng+" **:red[R]**"
      else:
        resultatstreng=resultatstreng+" **:blue[B]**"
        kvite=kvite+1
  else:
    for i in range(antall):
      kulenr=randint(1,len(eske))
      if eske[kulenr-1]==1:
        raude = raude+1
        resultatstreng=resultatstreng+" **:red[R]**"
      else:
        resultatstreng=resultatstreng+" **:blue[B]**"
        kvite=kvite+1
      eske.pop(kulenr-1)
      
tab1, tab2, tab3 = st.tabs(["Modell 1", "Modell 2", "Modell 3"])

with tab1:
  st.text("Denne modellen lar deg legge eit antal raude og blå kuler i ei eske, for så å trekkje ut eit visst antal. Dette kan gjentakast fleire gonger.")
  
  kuler_i_esken = int(st.number_input("Kor mange kuler er det i esken? (1-10000) ", min_value=1, value=6))
  raude_i_esken = int(st.number_input("Kor mange raude kuler er det? ", min_value=1, max_value=kuler_i_esken))
  antall_som_trekkes = int(st.number_input("Kor mange skal trekkjast ut kvar gong? ", min_value=1, value=6))
  attat=st.text_input("Skal du kunne legge tilbake kula du har trukket ut? (j/n) ", key=1, value="j")
  if attat=="j" or attat=="J":
    tilbakelegging=True
  else:
    tilbakelegging=False
  antall_simuleringar = int(st.number_input("Kor mange simuleringar vil du gjennomføre? ", min_value=1, max_value=10000, value=10))
  resultater=[]

  if st.button("Go!", key=2):
      for j in range(antall_simuleringar):
        resultatstreng=" "
        eske = []
        for i in range(kuler_i_esken):
          eske.append(0)
        for j in range(raude_i_esken):
          eske[j]=eske[j]+1
        raude=0
        kvite=0
        trekk(antall_som_trekkes)
        if antall_simuleringar<11:
          st.markdown(resultatstreng)
          st.write("Totalt ", raude, "raude og", kvite, "blå.")
        resultater.append(raude)
      skriv_regnskap(resultater, 1, antall_simuleringar)

      kat=[]
      val=[]
      for k in range(antall_som_trekkes+1):
        a = sum(1 for i in resultater if i  == k) 
        kat.append(k)
        val.append(a)
      st.bar_chart(val, x_label="Antal raude", y_label="Antal gongar", )

with tab2:
  def trekk_mod2():
    if tilbakelegging2==True:
      kulenr=randint(1,len(eske))
      if eske[kulenr-1]==1:
        return True
      else:
        return False
    else:
      kulenr=randint(1,len(eske))
      if eske[kulenr-1]==1:
        return True
      else:
        eske.pop(kulenr-1)
        return False
  st.write("Denne modellen lar deg trekkje frå eska til du treffer på den første raude kula.")
  kuler_i_esken2 = int(st.number_input("Kor mange kuler er det i esken? (1-10000) ", min_value=1, value=100, key=21))
  raude_i_esken2 = int(st.number_input("Kor mange raude kuler er det? " ,min_value=1, max_value=kuler_i_esken2, key=22))
  #attat2=st.text_input("Skal du kunne legge tilbake kula du har trukket ut? (j/n) ", placeholder="j")
  #if attat2=="j" or attat2=="J":
  #  tilbakelegging2=True
  #else:
  tilbakelegging2=False
  antall_simuleringar2 = int(st.number_input("Kor mange simuleringar vil du gjennomføre? ", min_value=1, max_value=10000, value=2, key=23))
  resultater2=[]

  if st.button("Go!"):
    for i in range(antall_simuleringar2):
      teller=1
      resultatstreng2=""
      eske = []
      for k in range(kuler_i_esken2):
        eske.append(0)
      for j in range(raude_i_esken2):
        eske[j]=eske[j]+1
      while not trekk_mod2():
        if antall_simuleringar2<30:
          resultatstreng2=resultatstreng2+" **:blue[B]**"
        teller=teller+1
      resultater2.append(teller)
      if antall_simuleringar2<30:
        resultatstreng2=resultatstreng2+" **:red[R]**"
        st.write(resultatstreng2)
        if antall_simuleringar2<20:
          st.write("Du måtte trekke",teller, "gongar før du fekk den første raude.")
    skriv_regnskap(resultater2, 2, antall_simuleringar2)
 

  # Data for plotting

  #kat=[]
  #val=[]
  #for k in range(len(resultater)):
  #      a = sum(1 for i in resultater if i  == k)
  ##      kat.append(k)
  #      val.append(a)
  
with tab3:
  st.write("Modell tre lar deg trekkje frå eska til alle raude er trekt ut.")
  
  def trekk3():
    kulenr=randint(1,len(eske))
    if eske[kulenr-1]==1:
      return True
    else:
      eske.pop(kulenr-1)
      return False

  kuler_i_esken3 = int(st.number_input("Kor mange kuler er det i esken? (1-10000) ", min_value=1, value=100, key=31))
  raude_i_esken3 = int(st.number_input(f"Kor mange raude kuler er det? (Færre enn {kuler_i_esken3+1}) ",min_value=1, value=5, key=32))
  antall_simuleringar3 = int(st.number_input("Kor mange simuleringar vil du gjere? ", key=33, min_value=1, value=2, max_value=10000))
  resultater3=[]

  if st.button("Go!", key=3):
    for i in range(antall_simuleringar3):
      resultatstreng3=""
      tell_raude=1
      antall_trekk=1
      eske = []
      for k in range(kuler_i_esken3):
        eske.append(0)
      for j in range(raude_i_esken3):
        eske[j]=eske[j]+1

      while tell_raude<raude_i_esken3:
        if trekk3():
          tell_raude=tell_raude+1
          resultatstreng3=resultatstreng3+" **:red[R ]**"
        else:
          resultatstreng3=resultatstreng3+" **:blue[B]**"
        antall_trekk=antall_trekk+1

      resultater3.append(antall_trekk)
      resultatstreng3=resultatstreng3 + " **:red[R]**"
      if antall_simuleringar3<20:
        st.write(resultatstreng3)
        st.write("Du måtte trekke",antall_trekk, "gongar for å trekkje alle dei ", raude_i_esken3, "raude.") 
    
    skriv_regnskap(resultater3, 3, antall_simuleringar3)
