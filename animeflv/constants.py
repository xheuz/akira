# constants
LAST_EPISODES = "LAST_EPISODES"
CURRENT_ANIMES = "CURRENT_ANIMES"
LAST_ANIME_ADDED = "LAST_ANIME_ADDED"

SELECTORS = {
    LAST_EPISODES: ["a", {"class_": "fa-play"}],
    CURRENT_ANIMES: "a.fa-play-circle",
    LAST_ANIME_ADDED: "article.Anime",
}
