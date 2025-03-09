import streamlit as st
from random import *
from statistics import *

st.text("Kugle kugler online 1.0")

def gjennomsnitt(lst):
  return mean(lst)

def typetal(lst):
  return mode(lst)

def varians(lst):
  return(variance(lst))

def skriv_regnskap(lst, modell):
  st.text("-----")
  if len(lst)<150:
    st.text("Liste over resultat: ")
    st.text(lst)
  var=variance(lst)
  std=var**0.5
  st.write("Typetalet er ", typetal(lst))
  st.write(f"Gjennomsnittet er {gjennomsnitt(lst): .2f}")
  st.write(f"Varians: {var: .2f}")
  st.write(f"Standardavvik: {std: .2f}")
  st.text("")
  if modell==1:
    if antall_som_trekkes<50: #Skriver ut kor mange gonger dei forskjellige verdiane dukket opp, dersom det er mindre enn 50 kuler
     for k in range(antall_som_trekkes+1):
       st.write("Antall ganger du trakk ", k, "raude : ", sum(1 for i in lst if i  == k))
     st.write(":sunglasses:")

def trekk(antall=1):
  global raude
  global kvite
  if tilbakelegging==True:
    for i in range(antall):
      kulenr=randint(1,len(eske))
      if eske[kulenr-1]==1:
        raude = raude+1
        if antall_simuleringar<11:
          st.write("R",sep="") # return kulenr, "R"
      else:
        if antall_simuleringar<11:
          st.write("K",sep="") # return kulenr, "K"
        kvite=kvite+1
  else:
    for i in range(antall):
      kulenr=randint(1,len(eske))
      if eske[kulenr-1]==1:
        raude = raude+1
        if antall_simuleringar<11:
          st.write("R ",end="") # return kulenr, "R"
      else:
        if antall_simuleringar<11:
          st.write("K ",end="") # return kulenr, "K"
        kvite=kvite+1
      eske.pop(kulenr-1)
      

#---- set up -----
kuler_i_esken = int(st.number_input("Kor mange kuler er det i esken? (1-10000) ", min_value=1))
raude_i_esken = int(st.number_input("Kor mange raude kuler er det? ", min_value=1))
antall_som_trekkes = int(st.number_input("Kor mange skal trekkjast ut kvar gong? ", min_value=1))
attat=st.text_input("Skal du kunne legge tilbake kula du har trukket ut? (j/n) ")
if attat=="j" or attat=="J":
  tilbakelegging=True
else:
  tilbakelegging=False
antall_simuleringar = int(st.number_input("Kor mange simuleringar vil du gjennomføre? ", min_value=1))

resultater=[]

st.write(tilbakelegging)
#--- main run ----

if st.button("Go!"):
    for j in range(antall_simuleringar):
      eske = []
      for i in range(kuler_i_esken):
        eske.append(0)
      for j in range(raude_i_esken):
        eske[j]=eske[j]+1
      raude=0
      kvite=0
      trekk(antall_som_trekkes)
      if antall_simuleringar<11:
        st.write(" ")
        st.write("Totalt ", raude, "raude og", kvite, "kvite.")
      resultater.append(raude)
    skriv_regnskap(resultater, 1)
