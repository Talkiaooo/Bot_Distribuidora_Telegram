import telebot
from telebot import types
from memoria import GestorMemoria
from chatbot import procesar_logica, obtener_lista_productos, obtener_promos

TOKEN = "8869509442:AAE_LTcTDeid5MnV8FhX8zi9SP0Yz2f7N3Q"
bot = telebot.TeleBot(TOKEN)
memoria_global = GestorMemoria()

def mostrar_menu(chat_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📦 Bebidas", callback_data="cat_bebidas"))
    markup.add(types.InlineKeyboardButton("📦 Almacen", callback_data="cat_almacen"))
    markup.add(types.InlineKeyboardButton("📦 Limpieza", callback_data="cat_limpieza"))
    markup.add(types.InlineKeyboardButton("🔥 Ver Promos", callback_data="ver_promos"))
    bot.send_message(chat_id, "Elige una opción:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(m):
    memoria_global.sesiones[m.chat.id] = {"estado": "REGISTRO", "paso": "NOMBRE", "datos": {}}
    bot.reply_to(m, "¡Hola! Decime tu nombre para empezar:")

@bot.callback_query_handler(func=lambda call: True)
def botones(call):
    # 1. RESPUESTA INMEDIATA: Cerramos el botón para que no salga el error 400
    bot.answer_callback_query(call.id)
    
    chat_id = call.message.chat.id
    
    # 2. PROCESAMIENTO
    try:
        if call.data.startswith("cat_"):
            cat = call.data.split("_")[1]
            bot.send_message(chat_id, obtener_lista_productos(cat), parse_mode="Markdown")
        elif call.data == "ver_promos":
            bot.send_message(chat_id, obtener_promos(), parse_mode="Markdown")
        
        # Después de mostrar el resultado, preguntamos qué desea consultar
        bot.send_message(chat_id, "¿Deseás consultar algo más o ver otro producto?")
    except Exception as e:
        print(f"Error: {e}")

@bot.message_handler(func=lambda m: True)
def manejar(m):
    chat_id = m.chat.id
    sesion = memoria_global.obtener(chat_id)
    
    # Procesamos la intención mediante el modelo de PLN
    resultado = procesar_logica(m.text, sesion)
    
    # Lógica de despacho de intenciones
    if resultado == "INTENCION_PROMOS":
        bot.reply_to(m, obtener_promos(), parse_mode="Markdown")
    elif resultado == "INTENCION_MENU":
        mostrar_menu(chat_id)
    elif resultado and resultado.startswith("INTENCION_CAT_"):
        cat = resultado.split("_")[2].lower()
        bot.reply_to(m, obtener_lista_productos(cat), parse_mode="Markdown")
    elif resultado: # Es parte del registro
        bot.reply_to(m, resultado)
    else:
        bot.reply_to(m, "No entendí eso. ¿Qué deseas consultar?")
        mostrar_menu(chat_id)

print("Bot iniciado correctamente...")
bot.polling(none_stop=True)