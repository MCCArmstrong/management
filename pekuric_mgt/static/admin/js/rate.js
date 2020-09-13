//Initial Ratings


const ratings = {
    facial-serum: 4.7,
    anti-perspirant: 3.4,
    sunscreen: 2.3
}

//Total Rating stars
const starsTotal = 5;

//Run getRatings when DOM Loads
document.addEventListener('DOMContentLoaded', getRatings);

function getRatings(){
    for(let rating in ratings){
        console.log(rating);
    }

}