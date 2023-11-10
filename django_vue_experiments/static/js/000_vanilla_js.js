jQuery(function () {
  var getCounterValue = function () {
    return parseInt($('#counter').text(), 10);
  };

  var setCounterValue = function (value) {
    $('#counter').text(value);
  };

  $('#decrement').on('click', function () {
    var oldValue = getCounterValue();
    var newValue = (oldValue -= 1);
    setCounterValue(newValue);
  });

  $('#increment').on('click', function () {
    var oldValue = getCounterValue();
    var newValue = (oldValue += 1);
    setCounterValue(newValue);
  });
});
