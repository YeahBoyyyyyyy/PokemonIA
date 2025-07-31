class Colors:
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
