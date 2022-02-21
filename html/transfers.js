const {Client} =  require("pg")

const client = new Client({
  user: "postgres",
  host: "localhost",
  database: "football_db",
  password: "taunus48",
  port: 5432,
});

client.connect();

    client.query(`
    SELECT l.latitude, l.longitude
    FROM locations l
    JOIN league_countries c ON c.country = l.country
    JOIN transfers t ON t.league_from = league_name
    WHERE season='2010-2011'`, 
    (err, res)=>{
        if(!err){
            console.log(res.rows);
        }else {
            console.log(err.message);
        }
        client.end;
    })


    // client.query(`
    // SELECT l.latitude, l.longitude
    // FROM locations l
    // JOIN league_countries c ON c.country = l.country
    // JOIN transfers t ON t.league_to = league_name`,
    //  (err, res)=>{
    //     if(!err){
    //         console.log(res.rows);
    //     }else {
    //         console.log(err.message);
    //     }
    //     client.end;
    // })




