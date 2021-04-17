$(document).ready(function() {
    $(function() {
    $('#datetimepicker6').datetimepicker();
    $('#datetimepicker').datetimepicker({
    useCurrent: false //Important! See issue #1075
    });
    $("#datetimepicker6").on("dp.change", function(e) {
    $('#datetimepicker').data("DateTimePicker").minDate(e.date);
    });
    $("#datetimepicker").on("dp.change", function(e) {
    $('#datetimepicker6').data("DateTimePicker").maxDate(e.date);
    });
    });
    });