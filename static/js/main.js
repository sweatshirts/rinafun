// "five down" easter egg as a reference to an arcade machine (twilight syndrome - murder case)
// found in danganronpa 2: goodbye despair
// i think its kinda rude you're inspect-elementin' find the damn eggs on your own next time!
var pattern = Array(5).fill('ArrowDown');
var current = 0;
var keyHandler = function (event) {

	if (pattern.indexOf(event.key) < 0 || event.key !== pattern[current]) {
		current = 0;
		return;
	}
	current++;
	if (pattern.length === current) {
		current = 0;
		window.alert("so you're looking for a true ending? sorry, you won't find it here!");
	}

};

document.addEventListener('keydown', keyHandler, false);


