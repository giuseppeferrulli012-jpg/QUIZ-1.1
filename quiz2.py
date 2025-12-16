# quiz.py (EX quiz_calcio_unico.py)

import streamlit as st
import random
# import pandas as pd # Non è necessario ma lo lasciamo commentato per chiarezza

# --- DATI DEL QUIZ: 50 DOMANDE (Completa qui le tue 50 domande!) ---
# Ogni elemento è un dizionario con 'Domanda', 'Corretta', 'Opzione 2', 'Opzione 3'.
ALL_QUIZ_QUESTIONS = [
    {
        "Domanda": "Quale allenatore ha vinto la Coppa dei Campioni/Champions League con tre club diversi?",
        "Corretta": "Carlo Ancelotti",
        "Opzione 2": "Pep Guardiola",
        "Opzione 3": "José Mourinho"
    },
    {
        "Domanda": "In che anno il Palermo ha giocato la sua unica finale di Coppa Italia?",
        "Corretta": "1974",
        "Opzione 2": "1979",
        "Opzione 3": "1982"
    },
    {
        "Domanda": "Qual è l'unico calciatore ad aver segnato in 7 competizioni internazionali diverse per club?",
        "Corretta": "Cristiano Ronaldo",
        "Opzione 2": "Lionel Messi",
        "Opzione 3": "Alfredo Di Stéfano"
    },
    {
        "Domanda": "Prima di allenare l'Arsenal, Arsène Wenger ha allenato una squadra giapponese. Quale?",
        "Corretta": "Nagoya Grampus Eight",
        "Opzione 2": "Gamba Osaka",
        "Opzione 3": "Urawa Red Diamonds"
    },
    {
        "Domanda": "Quale squadra detiene il record per il maggior numero di sconfitte consecutive in Serie A?",
        "Corretta": "Benevento",
        "Opzione 2": "Brescia",
        "Opzione 3": "Livorno"
    },
    {
        "Domanda": "Chi è l'unico portiere ad aver vinto il Pallone d'Oro senza aver mai giocato nel Milan, Inter o Juventus?",
        "Corretta": "Lev Yashin",
        "Opzione 2": "Gianluigi Buffon",
        "Opzione 3": "Sepp Maier"
    },
    {
        "Domanda": "In quale stadio il Milan ha vinto la sua prima Coppa dei Campioni nel 1963?",
        "Corretta": "Wembley",
        "Opzione 2": "San Siro",
        "Opzione 3": "Santiago Bernabéu"
    },
    {
        "Domanda": "Quale nazione africana fu la prima a raggiungere i quarti di finale di un Mondiale (nel 1990)?",
        "Corretta": "Camerun",
        "Opzione 2": "Nigeria",
        "Opzione 3": "Senegal"
    },
    {
        "Domanda": "Contro quale squadra Diego Armando Maradona ha segnato il suo primo gol in Serie A con il Napoli?",
        "Corretta": "Fiorentina",
        "Opzione 2": "Verona",
        "Opzione 3": "Udinese"
    },
    {
        "Domanda": "Qual è il club che ha vinto più Coppe Intercontinentali/Mondiali per Club?",
        "Corretta": "Real Madrid",
        "Opzione 2": "Milan",
        "Opzione 3": "Bayern Monaco"
    },
    # ----------------------------------------------------
    # AGGIUNGI QUI LE TUE 40 DOMANDE MANCANTI SE VUOI ARRIVARE A 50!
    # ----------------------------------------------------
]

# --- Configurazione della Pagina ---
st.set_page_config(
    page_title="QUIZ CALCIO IMPOSSIBILE ⚽",
    page_icon="🏆",
    layout="wide"
)

# --- Funzione per Iniziare o Resettare il Quiz ---
def initialize_quiz_state():
    """Imposta o resetta lo stato della sessione."""
    
    NUM_DOMANDE_DA_USARE = 10 
    
    if len(ALL_QUIZ_QUESTIONS) < NUM_DOMANDE_DA_USARE:
         NUM_DOMANDE_DA_USARE = len(ALL_QUIZ_QUESTIONS)
         
    st.session_state['questions'] = random.sample(ALL_QUIZ_QUESTIONS, NUM_DOMANDE_DA_USARE)
    
    st.session_state['question_index'] = 0
    st.session_state['score'] = 0
    st.session_state['quiz_finished'] = False
    st.session_state['feedback_message'] = ""
    st.session_state['current_question_key'] = random.randint(0, 1000000)

# --- Funzione per la Logica del Quiz ---
def check_answer(user_answer, correct_answer):
    """Verifica la risposta e aggiorna lo stato."""
    
    if st.session_state['feedback_message']:
        return
        
    if user_answer == correct_answer:
        st.session_state['score'] += 1
        st.session_state['feedback_message'] = "✅ Risposta Corretta!"
    else:
        st.session_state['feedback_message'] = f"❌ Risposta Errata. La risposta giusta era: **{correct_answer}**"
    
    # 🔄 MODIFICA APPLICATA QUI
    st.rerun() 

# --- Funzione per passare alla domanda successiva ---
def next_question():
    """Avanza all'indice successivo o termina il quiz."""
    st.session_state['question_index'] += 1
    st.session_state['feedback_message'] = ""
    st.session_state['current_question_key'] = random.randint(0, 1000000)

    if st.session_state['question_index'] >= len(st.session_state['questions']):
        st.session_state['quiz_finished'] = True
    
    # 🔄 MODIFICA APPLICATA QUI
    st.rerun() 


# --- Funzione Principale dell'App ---
def main():
    
    st.title("⚽ QUIZ CALCIO IMPOSSIBILE 🏆")
    st.markdown("Metti alla prova la tua conoscenza calcistica con domande da vero esperto.")

    if 'quiz_finished' not in st.session_state:
        initialize_quiz_state()
    
    NUM_DOMANDE = len(st.session_state.get('questions', []))
    
    # --- Schermata Finale del Quiz ---
    if st.session_state.get('quiz_finished', False):
        st.balloons()
        st.success("🎉 QUIZ COMPLETATO! 🎉")
        final_score = st.session_state['score']
        
        st.markdown(f"## Il tuo punteggio finale: **{final_score} / {NUM_DOMANDE}**")
        
        if final_score == NUM_DOMANDE:
            st.markdown("🤯 **SEI UN VERO ESPERTO ASSOLUTO! Complimenti!**")
        elif final_score >= NUM_DOMANDE * 0.7:
            st.markdown("⭐ **Eccellente! Sei quasi un Guru del Calcio!**")
        elif final_score >= NUM_DOMANDE * 0.4:
            st.markdown("👍 **Buon lavoro, ma c'è ancora molto da studiare!**")
        else:
            st.markdown("😬 **Devi riguardare la storia del calcio... o forse le domande erano *davvero* troppo difficili!**")
        
        st.button("Ricomincia il Quiz", on_click=initialize_quiz_state, type="primary")
        return

    # --- Visualizzazione del Quiz in Corso ---
    
    q_index = st.session_state['question_index']
    current_q_data = st.session_state['questions'][q_index]
    
    question_text = current_q_data['Domanda']
    correct_answer = current_q_data['Corretta']
    
    options = [current_q_data['Corretta'], current_q_data['Opzione 2'], current_q_data['Opzione 3']]
    random.shuffle(options)
    
    # Intestazione e Punteggio
    st.header(f"Domanda {q_index + 1} di {NUM_DOMANDE}")
    st.markdown(f"Punteggio attuale: **{st.session_state['score']}**")
    st.markdown("---")

    # Domanda
    st.subheader(question_text)
    
    # Selezione dell'utente
    user_choice = st.radio(
        "Seleziona la tua risposta:",
        options,
        index=None,
        key=st.session_state['current_question_key']
    )
    
    # Logica di risposta
    col1, col2 = st.columns(2)
    
    with col1:
        if user_choice and not st.session_state['feedback_message']:
            st.button("Conferma Risposta", 
                      on_click=check_answer, 
                      args=(user_choice, correct_answer), 
                      type="primary")
        
        elif st.session_state['feedback_message']:
            st.button("Domanda Successiva >>", on_click=next_question, type="secondary")


    # Visualizzazione del Feedback
    with col2:
        if st.session_state['feedback_message']:
            if "Corretta" in st.session_state['feedback_message']:
                st.success(st.session_state['feedback_message'])
            else:
                st.error(st.session_state['feedback_message'], icon="⚠️")


# Avvio dell'applicazione
if __name__ == "__main__":
    main()
