class Colors:
    # --- Text Styles ---
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
    GRAY        = '\033[90m'  # Texte gris (noir clair)
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

    RESET = '\033[0m'
    BOLD = '\033[1m'

    # Foreground text colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    GREY = '\033[90m'
    WHITE = '\033[97m'
    SUNNY = '\033[38;5;214m'
    RAIN = '\033[38;5;39m'
    SNOW = '\033[38;5;159m'
    SANDSTORM = '\033[38;5;223m'
    WALL = '\033[38;5;198m'
    WALL_TITLE = '\033[38;5;207m'
    STEALTH_ROCK = '\033[38;5;136m'
    TOXIC_SPIKES = '\033[38;5;93m'
    SPIKES = '\033[38;5;216m'
    STICKY_WEB = '\033[38;5;64m'
    TEAM1 = '\033[38;5;27m'
    TEAM2 = '\033[38;5;196m'


    @staticmethod
    def color_hp(hp_ratio: float) -> str:
        """Return ANSI color based on HP percentage (0.0 to 1.0)."""
        if hp_ratio > 0.6:
            return Colors.GREEN
        elif hp_ratio > 0.3:
            return Colors.YELLOW
        else:
            return Colors.RED

    @staticmethod
    def color_weather(weather: str) -> str:
        if weather == "Sunny":
            return Colors.SUNNY
        elif weather == "Rain":
            return Colors.RAIN
        elif weather == "Snow":
            return Colors.SNOW
        elif weather == "Sandstorm":
            return Colors.SANDSTORM
        
    @staticmethod
    def menu_option(index: int, label: str) -> str:
        color_map = {
            1: Colors.RED,
            2: Colors.BLUE,
            3: Colors.CYAN,
            4: Colors.GREY
        }
        color = color_map.get(index, Colors.WHITE)
        return f"{color}{index}. {label}{Colors.RESET}"
def print_color():
    for i in range(256):
        print(f"\033[38;5;{i}m{i:3d} \033[0m", end=' ')
        if (i + 1) % 16 == 0:
            print()
