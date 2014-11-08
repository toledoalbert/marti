function getFilteredTweets(wordsArray, positive, negative, neutral, past, present, future, geocode) {
	
	words = concatWords(wordsArray);

	//Make a call with these parameters

	//Return an array of integers that are the id's of resulting tweets
	response = [20, 54, 234, 34, 54, 65, 23, 75];
}

function getTweets(wordsArray, geocode) {

	words = concatWords(wordsArray);

	//make a call with the words given

	//return the array of objects that contain tweet information
	response = [

		{id: 23, context: "positive", tense: "present", frequentWord: "cloudy"},
		{id: 654, context: "negative", tense: "past", frequentWord: "cloudy"},
		{id: 345, context: "positive", tense: "present", frequentWord: "cloudy"},
		{id: 76, context: "neutral", tense: "future", frequentWord: "cloudy"},
		{id: 2563, context: "positive", tense: "past", frequentWord: "cloudy"},
		{id: 2345, context: "negative", tense: "past", frequentWord: "cloudy"}

	];

}


function concatWords(wordsArray) {

	wordsArray = ["cloudy", "rainy", "cold", "windy", "sunny", "hot", "warm", "chilly"];

	words = "";

	//Concatanate the words together for the request.
	for (var i = wordsArray.length - 1; i >= 0; i--) {
		if(i == 0){
			words += wordsArray[i];
		} else{
			words += wordsArray[i] + "+";
		}
	};

	return words;
}