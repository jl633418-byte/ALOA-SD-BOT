import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Lista de más de 150 palabras y frases prohibidas
MALAS_PALABRAS = [
    # Básicas y muy comunes
    "puta", "puto", "putas", "putos", "putita", "putito", "putilla", "putillo",
    "mierda", "mierdas", "mierdita", "mierdota",
    "coño", "coños", "concha", "conchas", "conchudo", "conchuda",
    "cabrón", "cabron", "cabrona", "cabrones", "cabronazo", "cabronaza",
    "joder", "jodido", "jodida", "jodete", "jódete", "joderte",
    "gilipollas", "gilipolla", "gilipollez",
    "hijo de puta", "hija de puta", "hijoputa", "hijaputa", "hdp", "hp",
    "la puta", "la puta madre", "puta madre", "putamadre",
    
    # Genitales y sexuales
    "verga", "vergas", "vergota", "verguita", "vergazo",
    "polla", "pollas", "pollón", "polludo", "polluda",
    "pija", "pijas", "pijudo", "pijuda",
    "pito", "pitos", "pitito", "pitazo",
    "pene", "penes", "penecito",
    "vagina", "vaginas", "chocha", "chochas", "chocho", "chochos",
    "cojones", "cojón", "cojonudo", "cojonuda",
    "huevos", "huevón", "huevon", "huevona", "huevosos",
    "pelotas", "pelotudo", "pelotuda",
    "culo", "culos", "culito", "culote", "culero", "culera", "culiado", "culear",
    "ano", "anos", "ojete", "ojetes",
    "tetas", "teta", "tetitas", "tetazas", "chiches", "chichis",
    "pechos", "pechitos",
    
    # Insultos fuertes
    "maricón", "maricon", "maricones", "marica", "maricas", "maricónazo",
    "puto de mierda", "puta de mierda",
    "imbécil", "imbecil", "idiota", "estupido", "estúpido", "estupida", "estúpida",
    "pendejo", "pendeja", "pendejos", "pendejas", "pendejada",
    "boludo", "boluda", "boludos", "boludas",
    "tarado", "tarada", "tarados",
    "retrasado", "retrasada", "mongólico", "mongolica", "mongolo",
    "subnormal", "deficientes",
    "zorra", "zorras", "zorro", "perra", "perras", "perro de mierda",
    "cerdo", "cerda", "puerco", "puerca",
    "basura", "escoria", "desecho",
    
    # Mexicanismos y latinos
    "chingar", "chingada", "chingado", "chingados", "chingadas",
    "chinga tu madre", "chingatumadre", "ctm", "ptm",
    "pinche", "pinches", "pinche puto", "pinche puta",
    "culero", "culera", "culeros",
    "guey", "güey", "wey", "we", "weon", "weona", "weones",
    "conchetumare", "conchesumare", "ctm",
    "aweonao", "aweoná", "weonao",
    "pajero", "pajera", "paja", "pajear", "pajearse",
    "mamón", "mamon", "mamona", "mamar", "mamada", "mamadas",
    "chupar", "chupapollas", "chupavergas",
    
    # Españoles / Argentinos / otros
    "hostia", "hostias", "ostia", "me cago en", "mecagoen",
    "carajo", "carajos", "carajote",
    "joder", "joderse", "me jodió",
    "gil", "gila", "gilazo",
    "capullo", "capullos",
    "tocaplotas", "tocahuevos",
    "soplapollas", "chupapijas",
    "malparido", "malparida", "malnacido", "malnacida",
    "hijueputa", "hijueputas",
    "gonorrea", "gonorreas",
    "sapo", "sapas", "sapo hijueputa",
    
    # Inglés comunes
    "fuck", "fucking", "fucker", "fuckers", "motherfucker", "motherfuckers",
    "shit", "shitty", "bullshit",
    "bitch", "bitches", "son of a bitch",
    "asshole", "assholes", "ass", "asses",
    "dick", "dicks", "dickhead",
    "pussy", "pussies",
    "cunt", "cunts",
    "cock", "cocks", "cock sucker", "cocksucker",
    "whore", "whores", "slut", "sluts",
    "bastard", "bastards",
    
    # Variaciones y abreviaturas
    "ptm", "ctm", "hdp", "hp", "mlc", "mrd", "vrg", "vrga",
    "pnche", "piche", "picha", "pichas",
    "culiau", "culeao", "culeada",
    "conchatumadre", "conchasumadre",
    "la concha de tu madre", "laconchadetumadre",
    "me cago en dios", "mecagoendios", "me cago en la puta",
    "hijo de la gran puta", "hija de la gran puta",
    "puto amo", "puta amo",
    "re puta", "reputa", "re puto", "reputo",
    "la puta que te parió", "laputaquetepario",
    "andate a la mierda", "vete a la mierda", "vetealmierda"
]

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")
    print(f"🔍 Filtrando {len(MALAS_PALABRAS)} palabras prohibidas")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    contenido = message.content.lower()
    contiene_mala = any(palabra in contenido for palabra in MALAS_PALABRAS)

    if contiene_mala:
        try:
            await message.delete()
            await message.channel.send(f"🚫 {message.author.mention}, ese mensaje contenía lenguaje inapropiado.")
            print(f"🗑️ Mensaje eliminado de {message.author}: {message.content}")
        except discord.Forbidden:
            print("❌ No tengo permisos para borrar mensajes")
        except Exception as e:
            print(f"❌ Error: {e}")

    await bot.process_commands(message)

# Lee el token de la variable de entorno
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("No se encontró la variable DISCORD_TOKEN")

bot.run(TOKEN)
