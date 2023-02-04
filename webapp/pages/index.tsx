const images = ['https://static.bunnycdn.ru/i/cache/images/9/9f/9f4855db98bb6923ea807bf2bdbdc3dd.jpg', 'https://static.bunnycdn.ru/i/cache/images/7/74/74380843242f2c6a8ae40b02b9b428f9.jpg', "https://static.bunnycdn.ru/i/cache/images/e/ea/ea568325c46915dcff46685d768ec8bf.jpg", "https://static.bunnycdn.ru/i/cache/images/2/2b/2b0da67729cf5065eab5088140b589da.jpg"]

const cardData = {
  name: "World Trigger",
  name_translation: null,
  episodes: 12,
  source: "9anime",
  synopsis: "After successfully holding off the invasion by Aftokrator, the Border Defense Agency prepares an away mission into the Neighbor's dimension. However, like in previous scouting expeditions, only A-rank teams are certain to secure a spot. As the B-rank wars continue, Osamu Mikumo and the rest of Tamakoma-2 quickly fight to the top in an attempt to obtain a promotion before the operation begins.Meanwhile, a new Neighbor ship approaches Border Headquarters. Noticing that the attackers are targeting the Border Expedition Ship, forces are hastily sent to combat them. However, with fewer squads available due to the proceeding rank wars, the organization is sent into disarray. This latest offensive from the Neighbors shrouds the fate of the all-important expedition ship in uncertainty.",
  score: 8.07,
  score_amount_users: 48868,
  ranked: 1423,
  thumbnail: "https://static.bunnycdn.ru/i/cache/images/2/2b/2b0da67729cf5065eab5088140b589da.jpg",
  cover: "https://static.bunnycdn.ru/i/cache/images/2/2b/2b0da67729cf5065eab5088140b589da.jpg",
  last_released: new Date(),
  status: "Releasing"
}

const AnimeCard = (anime) => {
  return (
  <div className="bg-white">
    <img src={anime.thumbnail} alt={anime.name} />
    <h4>{anime.name}</h4>
    <div>{anime.score}/10 (based on {anime.score_amount_users} reviews)</div>
  </div>)
}

export default function Home() {
  return (
    <div className="bg-slate-100">
      {/* <div className="container">
        <input placeholder="Search"/>
      </div> */}
      <div className="p-4">
        <AnimeCard {...cardData} />
        <ul>
          <li>
          </li>
        </ul>
      </div>
    </div>
  )
}
