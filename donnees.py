class bcolors:

    GRAY = '\033[90m'
    # --- Text Styles ---
    ENDC = '\033[0m'  # Réinitialise tous les styles et couleurs
    BOLD          = '\033[1m'   # Texte en gras
    UNBOLD = '\033[22m'
    DIM           = '\033[2m'   # Texte atténué (moins lumineux, utile pour indiquer que c’est secondaire)
    ITALIC        = '\033[3m'   # Texte en italique (pas pris en charge partout)
    UNDERLINE     = '\033[4m'   # Texte souligné
    BLINK         = '\033[5m'   # Texte clignotant (rarement pris en charge)
    REVERSE       = '\033[7m'   # Inverse les couleurs (texte devient fond, fond devient texte)
    HIDDEN        = '\033[8m'   # Texte caché (visible uniquement en le copiant)
    STRIKETHROUGH = '\033[9m'   # Texte barré (pas toujours pris en charge)

    # --- Text Colors (Foreground) ---
    BLACK       = '\033[30m'  # Texte noir
    DARK_RED         = '\033[31m'  # Texte rouge
    GREEN       = '\033[32m'  # Texte vert
    YELLOW      = '\033[33m'  # Texte jaune
    BLUE        = '\033[34m'  # Texte bleu
    MAGENTA     = '\033[35m'  # Texte magenta (rose/violet)
    CYAN        = '\033[36m'  # Texte cyan (bleu clair)
    WHITE       = '\033[37m'  # Texte blanc (ou gris clair selon le terminal)
    DEFAULT     = '\033[39m'  # Couleur de texte par défaut du terminal
    ORANGE = '\033[38;5;208m'  # Texte orange (ANSI 256 couleurs)

    # --- Bright Text Colors ---
    LIGHT_BLACK   = '\033[90m'  # Gris foncé (noir lumineux)
    OKRED = '\033[91m'  # Rouge clair
    LIGHT_RED = '\033[91m'
    OKGREEN = '\033[92m'  # Vert clair
    LIGHT_GREEN = '\033[92m'
    OKYELLOW = '\033[93m'  # Jaune clair
    LIGHT_YELLOW = '\033[93m'  # Jaune clair
    OKBLUE    = '\033[94m'  # Bleu clair
    LIGHT_BLUE = '\033[94m'
    OKMAGENTA = '\033[95m'  # Magenta clair
    OKCYAN    = '\033[96m'  # Cyan clair
    OKWHITE   = '\033[97m'  # Blanc vif

    # --- Background Colors ---
    BG_BLACK     = '\033[40m'  # Fond noir
    BG_RED       = '\033[41m'  # Fond rouge
    BG_GREEN     = '\033[42m'  # Fond vert
    BG_YELLOW    = '\033[43m'  # Fond jaune
    BG_BLUE      = '\033[44m'  # Fond bleu
    BG_MAGENTA   = '\033[45m'  # Fond magenta
    BG_CYAN      = '\033[46m'  # Fond cyan
    BG_WHITE     = '\033[47m'  # Fond blanc
    BG_DEFAULT   = '\033[49m'  # Fond par défaut du terminal

    # --- Bright Background Colors ---
    BG_BRIGHT_BLACK   = '\033[100m'  # Fond gris foncé
    BG_BRIGHT_RED     = '\033[101m'  # Fond rouge clair
    BG_BRIGHT_GREEN   = '\033[102m'  # Fond vert clair
    BG_BRIGHT_YELLOW  = '\033[103m'  # Fond jaune clair
    BG_BRIGHT_BLUE    = '\033[104m'  # Fond bleu clair
    BG_BRIGHT_MAGENTA = '\033[105m'  # Fond magenta clair
    BG_BRIGHT_CYAN    = '\033[106m'  # Fond cyan clair
    BG_BRIGHT_WHITE   = '\033[107m'  # Fond blanc vif


POKEMON_TYPES = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel",
              "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy", "Null"]

POKEMON_TYPES_ID = {"Normal":0, "Fighting":1, "Flying":2, "Poison":3, "Ground":4, "Rock":5, "Bug":6, 
                    "Ghost":7, "Steel":8, "Fire":9, "Water":10, "Grass":11, "Electric":12, "Psychic":13, 
                    "Ice":14, "Dragon":15, "Dark":16, "Fairy":17, "Null":18}

TERRAIN = ["Grassy Terrain", "Electric Terrain", "Psychic Terrain", "Misty Terrain", "None"]

WEATHER = ["Sunny", "Rainy", "Snow", "Sandstorm", "None"]



type_chart = [
    # Normal  Fight  Fly  Pois  Grou  Rock  Bug   Ghos  Stee  Fire  Wate  Gras  Elec  Psyc  Ice   Drag  Dark  Fair
    [  1.0,   1.0,  1.0,  1.0,  1.0,  0.5,  1.0,  0.0,  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0],  # Normal
    [  2.0,   1.0,  0.5,  0.5,  1.0,  2.0,  0.5,  0.0,  2.0,  1.0,  1.0,  1.0,  1.0,  0.5,  2.0,  1.0,  2.0,  0.5],  # Fighting
    [  1.0,   2.0,  1.0,  1.0,  1.0,  0.5,  2.0,  1.0,  0.5,  1.0,  1.0,  2.0,  0.5,  1.0,  1.0,  1.0,  1.0,  1.0],  # Flying
    [  1.0,   1.0,  1.0,  0.5,  0.5,  0.5,  1.0,  0.5,  0.0,  1.0,  1.0,  2.0,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0],  # Poison
    [  1.0,   1.0,  0.0,  2.0,  1.0,  2.0,  0.5,  1.0,  2.0,  2.0,  1.0,  0.5,  2.0,  1.0,  1.0,  1.0,  1.0,  1.0],  # Ground
    [  1.0,   0.5,  2.0,  1.0,  0.5,  1.0,  2.0,  1.0,  0.5,  2.0,  1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  1.0,  1.0],  # Rock
    [  1.0,   0.5,  0.5,  0.5,  1.0,  1.0,  1.0,  0.5,  0.5,  0.5,  1.0,  2.0,  1.0,  2.0,  1.0,  1.0,  2.0,  0.5],  # Bug
    [  0.0,   1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  1.0,  0.5,  1.0],  # Ghost
    [  1.0,   1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  1.0,  0.5,  0.5,  0.5,  1.0,  0.5,  1.0,  2.0,  1.0,  1.0,  2.0],  # Steel
    [  1.0,   1.0,  1.0,  1.0,  1.0,  0.5,  2.0,  1.0,  2.0,  0.5,  0.5,  2.0,  1.0,  1.0,  2.0,  0.5,  1.0,  1.0],  # Fire
    [  1.0,   1.0,  1.0,  1.0,  2.0,  2.0,  1.0,  1.0,  1.0,  2.0,  0.5,  0.5,  1.0,  1.0,  1.0,  0.5,  1.0,  1.0],  # Water
    [  1.0,   1.0,  0.5,  0.5,  2.0,  2.0,  0.5,  1.0,  0.5,  0.5,  2.0,  0.5,  1.0,  1.0,  1.0,  0.5,  1.0,  1.0],  # Grass
    [  1.0,   1.0,  2.0,  1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  0.5,  0.5,  1.0,  1.0,  0.5,  1.0,  1.0],  # Electric
    [  1.0,   2.0,  1.0,  2.0,  1.0,  1.0,  1.0,  1.0,  0.5,  1.0,  1.0,  1.0,  1.0,  0.5,  1.0,  1.0,  0.0,  1.0],  # Psychic
    [  1.0,   1.0,  2.0,  1.0,  2.0,  1.0,  1.0,  1.0,  0.5,  0.5,  0.5,  2.0,  1.0,  1.0,  0.5,  2.0,  1.0,  1.0],  # Ice
    [  1.0,   1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  0.0],  # Dragon
    [  1.0,   0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  1.0,  0.5,  0.5],  # Dark
    [  1.0,   2.0,  1.0,  0.5,  1.0,  1.0,  1.0,  1.0,  0.5,  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  2.0,  1.0]   # Fairy
]

nature_chart = {
    # key : nature / value : [1,1,1,1,1] ([atk, def, spa, spd, spe])
    # Reduced     Atk                          Def                      Spe. Atk                     Spe. Def                      Speed
    "Hardy": [1, 1, 1, 1, 1],  "Lonely": [1.1, 0.9, 1, 1, 1], "Adamant": [1.1, 1, 0.9, 1, 1],  "Naughty":[1.1, 1, 1, 0.9, 1], "Brave":   [1.1, 1, 1, 1, 0.9], # Atk Boosted
    "Bold":  [0.9, 1.1, 1, 1, 1], "Docile": [1, 1, 1, 1, 1],  "Impish":  [1, 1.1, 0.9, 1, 1],  "Lax":    [1, 1.1, 1, 0.9, 1], "Relaxed": [1, 1.1, 1, 1, 0.9], # Def Boosted
    "Modest":[0.9, 1, 1.1, 1, 1], "Mild":   [1, 0.9, 1.1, 1, 1], "Bashful": [1, 1, 1, 1, 1],   "Rash":   [1, 1, 1.1, 0.9, 1], "Quiet":   [1, 1, 1.1, 1, 0.9],   # Spe. Atk Boosted
    "Calm":  [0.9, 1, 1, 1.1, 1], "Gentle": [1, 0.9, 1, 1.1, 1], "Careful": [1, 1, 0.9, 1.1, 1],  "Quirky": [1, 1, 1, 1, 1],  "Sassy":   [1, 1, 1, 1.1, 0.9], # Spe. Def Boosted
    "Timid": [0.9, 1, 1, 1, 1.1], "Hasty":  [1, 0.9, 1, 1, 1.1], "Jolly":   [1, 1, 0.9, 1, 1.1],  "Naive":  [1, 1, 1, 0.9, 1.1], "Serious": [1, 1, 1, 1, 1], # Speed Boosted
}
    