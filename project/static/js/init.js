(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space

var sliders = document.getElementsByClassName('sliders');

var brightSlider = document.getElementById('slider-bright');

var checkbox = document.getElementById('switch');

for ( var i = 0; i < sliders.length; i++ ) {

    noUiSlider.create(sliders[i], {
        start: 127,
        connect: [true, false],
        orientation: "vertical",
        range: {
            'min': 0,
            'max': 255
        },
        format: wNumb({
        decimals: 0
        })
    });
}

noUiSlider.create(brightSlider, {
	connect: [true, false],
	orientation: "horizontal",
	start: 50,
	step: 10,
	range: {
		'min': 0,
		'max': 100
	}
});

function sendrgb () {

	var r = sliders[0].noUiSlider.get();
	var g = sliders[1].noUiSlider.get();
	var b = sliders[2].noUiSlider.get();
	var bright = brightSlider.noUiSlider.get();
	var state = checkbox.checked;
	jQuery.ajax({type: "PUT", url: lampapi.concat('?') + jQuery.param({"r": r, "g": g, "b": b, 'br': bright, 'sw': state})});
}

// Bind the color changing function
// to the slide event.

brightSlider.noUiSlider.on('set.one', sendrgb);
sliders[0].noUiSlider.on('set.one', sendrgb);
sliders[1].noUiSlider.on('set.one', sendrgb);
sliders[2].noUiSlider.on('set.one', sendrgb);

