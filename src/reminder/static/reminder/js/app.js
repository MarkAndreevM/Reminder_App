// Скрипт для Popup (формы заполнения уведомления) START

var popup1 = document.getElementById("popup-1")
var openPopup1 = document.getElementById("open-popup-1")
var closePopup1 = document.getElementById('close-popup-1')

openPopup1.addEventListener('click', () => {
	popup1.style.display = "block";
})

closePopup1.addEventListener('click', () => {
	popup1.style.display = "none";
})

// Скрипт для Popup (формы заполнения уведомления) END




 /*скрипта календаря START*/

 /* Локализация datepicker */
 $.datepicker.regional['ru'] = {
	closeText: 'Закрыть',
	prevText: 'Предыдущий',
	nextText: 'Следующий',
	currentText: 'Сегодня',
	monthNames: ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'],
	monthNamesShort: ['Янв','Фев','Мар','Апр','Май','Июн','Июл','Авг','Сен','Окт','Ноя','Дек'],
	dayNames: ['воскресенье','понедельник','вторник','среда','четверг','пятница','суббота'],
	dayNamesShort: ['вск','пнд','втр','срд','чтв','птн','сбт'],
	dayNamesMin: ['Вс','Пн','Вт','Ср','Чт','Пт','Сб'],
	weekHeader: 'Не',
	dateFormat: 'dd.mm.yy',
	firstDay: 1,
	isRTL: false,
	showMonthAfterYear: false,
	yearSuffix: ''
};
$.datepicker.setDefaults($.datepicker.regional['ru']);

$(function(){
	$("#datepicker").datepicker();
});

 /*скрипта календаря END*/





  /*скрипта времени START*/

$("input[name=time]").clockpicker({       
	placement: 'bottom',
	align: 'left',
	autoclose: true,
	default: 'now',
	donetext: "Select",
	init: function() { 
							console.log("colorpicker initiated");
						},
						beforeShow: function() {
							console.log("before show");
						},
						afterShow: function() {
							console.log("after show");
						},
						beforeHide: function() {
							console.log("before hide");
						},
						afterHide: function() {
							console.log("after hide");
						},
						beforeHourSelect: function() {
							console.log("before hour selected");
						},
						afterHourSelect: function() {
							console.log("after hour selected");
						},
						beforeDone: function() {
							console.log("before done");
						},
						afterDone: function() {
							console.log("after done");
						}
});

  /*скрипта времени END*/



  