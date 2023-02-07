const images = ['https://static.bunnycdn.ru/i/cache/images/9/9f/9f4855db98bb6923ea807bf2bdbdc3dd.jpg', 'https://static.bunnycdn.ru/i/cache/images/7/74/74380843242f2c6a8ae40b02b9b428f9.jpg', "https://static.bunnycdn.ru/i/cache/images/e/ea/ea568325c46915dcff46685d768ec8bf.jpg", "https://static.bunnycdn.ru/i/cache/images/2/2b/2b0da67729cf5065eab5088140b589da.jpg"]

const generateListOfElements = (item, length, property = "") => {
  function _propertyIncrement(_, i) {
    if (!property) return { ...item }
    return { ...item, [property]: i + 1 }
  }
  return [...Array.from({ length }, _propertyIncrement)]
}

// ratings
const RATINGS_MAPPING = {
  "G": {
    name: "General Audiences",
    description: "Nothing that would offend parents for viewing by children.",
    ages: "all"
  },
  "PG": {
    name: "Parental Guidance Suggested",
    description: "Parents urged to give “parental guidance.” May contain some material parents might not like for their young children.",
    ages: "all"
  },
  "PG-13": {
    name: "Parents Strongly Cautioned",
    description: "Parents are urged to be cautious. Some material may be inappropriate for pre-teenagers.",
    ages: "13+"
  },
  "R": {
    name: "Restricted",
    description: "Contains some adult material. Parents are urged to learn more about the film before taking their young children with them.",
    ages: "17+"
  },
  "NC-17": {
    name: "Clearly Adult",
    description: "Clearly adult. Children are not admitted.",
    ages: "18+"
  },
  "U": {
    name: "Unrated",
    description: "Not rated.",
    ages: ""
  }
}

const getRatingDetails = (rating: string) => RATINGS_MAPPING[rating]


// data
const episode = {
  number: 1,
  title: "Episode Title",
  aired: new Date().toDateString()
}

const anime = {
  title: "Anime Title",
  alternative_titles: {
    english: "Some translation"
  },
  episodes: generateListOfElements(episode, 12, "number"),
  rating: "PG-13",
  rating_details: getRatingDetails("R"),
  synopsis: "",
  season: 1,
  score: 10,
  score_by_users: 48868,
  ranked: 1423,
  thumbnail: "https://static.bunnycdn.ru/i/cache/images/2/2b/2b0da67729cf5065eab5088140b589da.jpg",
  cover: "https://static.bunnycdn.ru/i/cache/images/2/2b/2b0da67729cf5065eab5088140b589da.jpg",
  status: "Releasing",
  genres: ["comedy", "horror", "adventure"],
  sequel: null,
  prequel: null,
  related: [],
}

const animes = [anime]

console.log(animes)

const cardData = {
  name: "World Trigger",
  name_translation: null,
  episodes: 12,
  season: 1,
  current_episode: 4,
  provider: "9anime",
  rating: "NC-17",
  synopsis: "After successfully holding off the invasion by Aftokrator, the Border Defense Agency prepares an away mission into the Neighbor's dimension. However, like in previous scouting expeditions, only A-rank teams are certain to secure a spot. As the B-rank wars continue, Osamu Mikumo and the rest of Tamakoma-2 quickly fight to the top in an attempt to obtain a promotion before the operation begins.Meanwhile, a new Neighbor ship approaches Border Headquarters. Noticing that the attackers are targeting the Border Expedition Ship, forces are hastily sent to combat them. However, with fewer squads available due to the proceeding rank wars, the organization is sent into disarray. This latest offensive from the Neighbors shrouds the fate of the all-important expedition ship in uncertainty.",
  score: 8.07,
  score_amount_users: 48868,
  ranked: 1423,
  thumbnail: "https://static.bunnycdn.ru/i/cache/images/2/2b/2b0da67729cf5065eab5088140b589da.jpg",
  cover: "https://static.bunnycdn.ru/i/cache/images/2/2b/2b0da67729cf5065eab5088140b589da.jpg",
  released: new Date(),
  status: "Releasing",
  genres: ["comedy", "horror", "adventure"],
  seasons: [
    {
      number: 1,
      episodes: 12,
      released: new Date(),
      status: "Completed",
      sequel: null,
      prequel: null,
    }
  ]
}

const AnimeProfileHeader = ({ title, thumbnail, status, rating, score }) => {
  return (<div className="relative h-80 w-full bg-slate-500 rounded-[3rem] rounded-t-none overflow-hidden">
    <img className="absolute h-full w-full object-cover" src={thumbnail} alt={title} />
    <div className="absolute inset-0 flex items-end justify-center p-4 top-[50%] bg-gradient-to-b from-transparent to-black">
      <div className="w-full text-white text-center">
        <h3 className="font-semibold mb-4 text-xl text-shadow-outline shadow-black">{title}</h3>
        <div className="flex h-full justify-around px-4 items-center bg-gradient-to-b from-white via-gray-200 to-gray-900 text-transparent bg-clip-text font-bold text-sm">
          <span>{status}</span>
          <div className="flex min-w-[32px] justify-center items-center border border-white px-2 py-1 rounded-lg">
            <h4 className="text-xs">{rating}</h4>
          </div>
          <span>MAL {score}</span>
        </div>
      </div>
    </div>
  </div>)
}

const AnimeProfileAbout = ({ synopsis }) => {
  return (
    <>
      <Section title="About">
        <p className="text-sm text-justify">{synopsis}</p>
      </Section>
    </>
  )
}

type AnimeCardProps = {
  title: string
  thumbnail: string
}

const AnimeCard = ({ title, thumbnail }: AnimeCardProps) => {
  return (
    <div className="flex flex-col items-center cursor-pointer">
      <div className="border mb-1">
        <div className="h-56 w-40 relative pb-[100%] rounded-3xl overflow-hidden">
          <img className="absolute h-full w-full object-cover" src={thumbnail} alt={title} />
          <div className="absolute inset-0 flex items-end justify-center p-3 top-[75%] bg-gradient-to-b from-transparent to-slate-900"></div>
        </div>
      </div>
      <h5 className="text-sm font-semibold">{title}</h5>
    </div>
  )
}

type AnimeContinueWatchingCardProps = {
  thumbnail: string
  name: string
  season: number
  current_episode: number
}

const AnimeContinueWatchingCard = ({ thumbnail, name, season, current_episode }: AnimeContinueWatchingCardProps) => {
  return (
    <div className="border cursor-pointer">
      <div className="h-32 w-48 relative pb-[80%] rounded-3xl overflow-hidden">
        <img className="absolute h-full w-full object-cover" src={thumbnail} alt={name} />
        <div className="absolute inset-0 flex items-end justify-center p-4 top-[70%] bg-gradient-to-b from-transparent to-slate-900"></div>
      </div>
      {/* <div className="h-1 rounded-lg bg-gradient-to-r from-slate-500 via-slate-500 to-slate-300"></div> */}
      <div className="flex flex-col justify-center items-center pt-2">
        <h4 className="font-semibold text-lg">{name}</h4>
        <h6 className="text-sm">Season {season} &bull; Episode {current_episode}</h6>
      </div>
    </div>
  )
}

type SliderItemProps = {
  children: React.ReactNode
}

const SliderItem = ({ children }: SliderItemProps) => {
  return (
    <li className="min-w-48 snap-start">
      {children}
    </li>
  )
}

type SliderProps = {
  children: React.ReactNode
}

const Slider = ({ children }: SliderProps) => {
  return (
    <ul className="flex gap-3 overflow-y-auto snap-mandatory snap-x scrollbar-hide">
      {children}
    </ul>
  )
}

type SectionProps = {
  title: string
  amount?: number
  redirect?: string
  children: React.ReactNode
}

const Section = ({ children, title, amount, redirect }: SectionProps) => {
  const firstWord = title.split(' ').shift()
  const rest = title.split(' ').slice(1).join(' ')

  return (
    <section className="flex flex-col gap-4">
      <div className="flex items-center justify-between" role="heading">
        <h2 className="text-2xl">
          <span className="font-semibold">{firstWord}</span> {rest}
        </h2>
        {redirect && <a href={redirect}>See all {amount && amount} &gt;</a>}
      </div>
      {children}
    </section>
  )
}

export default function Home() {
  const c = Array.from({ length: 20 }, (_, i) => ({ ...anime, ["thumbnail"]: images[Math.abs(Math.round(i / (images.length + 2)))] }))

  return (
    <>
      <AnimeProfileHeader {...anime} />
      <div className="flex text-xs font-semibold justify-center py-1">{[cardData.released.toDateString(), cardData.ranked, ...cardData.genres].join(" ")}</div>
      <div className="min-h-[100vh] flex flex-col gap-4 p-2 overflow-hidden">
        <AnimeProfileAbout {...cardData} />
        <Section title="Episodes">
          <div className="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
            {anime.episodes.map((e, i) => (
              <div key={`${e.title}-${e.number}`} className="flex gap-4 items-center">
                <div className="relative p-8 overflow-hidden rounded-lg">
                  <img className="absolute inset-0" src={anime.thumbnail} />
                  <div className="absolute inset-0 bg-slate-900 opacity-80"></div>
                  <div className="absolute inset-0 flex items-center justify-center text-white text-xl font-semibold">{e.number}</div>
                </div>
                <div className="py-2">
                  <div className="text-xl">{e.title}</div>
                  <div className="text-xs">{e.aired}</div>
                </div>
              </div>
            ))}
          </div>
        </Section>
        <Section title="Episodes Season 2">
          <div>
            <div>image &bull; Epidose 1 &bull; watched</div>
            <div>image &bull; Epidose 2 &bull; watched</div>
          </div>
        </Section>

        <Section title="Continue Watching" redirect="#">
          <Slider>
            {c.map((card, i) => (
              <SliderItem key={`${card.title}-${i}`}>
                <AnimeContinueWatchingCard {...cardData} />
              </SliderItem>
            ))}
          </Slider>
        </Section>
        <Section title="Top Airing Anime" redirect="#" amount={11}>
          <Slider>
            {c.map((card, i) => (
              <SliderItem key={`${card.title}-${i}`}>
                <AnimeCard {...card} />
              </SliderItem>
            ))}
          </Slider>
        </Section>
        <Section title="Summer 2021 Anime" redirect="#" amount={11}>
          <Slider>
            {c.map((card, i) => (
              <SliderItem key={`${card.title}-${i}`}>
                <AnimeCard {...card} />
              </SliderItem>
            ))}
          </Slider>
        </Section>
        <Section title="Recommendations" redirect="#">
          <Slider>
            {c.map((card, i) => (
              <SliderItem key={`${card.title}-${i}`}>
                <AnimeCard {...card} />
              </SliderItem>
            ))}
          </Slider>
        </Section>
      </div>
    </>
  )
}
