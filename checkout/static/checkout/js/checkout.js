/*jshint esversion: 6 */
$(document).ready(
    // Run check all fields on document ready
    checkAllFields()
);
/**
 * This funtcion will change Country field syle
 * when value is different than default
 */
let countrySelected = $('#id_country').val();
if (!countrySelected) {
    $('#id_country').css('color', '#ced4da');
}
$('#id_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#ced4da');
    } else {
        $(this).css('color', '#495057');
    }
});

/**
 * This function will check every required
 * field and disable button if any of them is empty
 */
function checkAllFields() {
    $('#payment-form input[required]').each(function () {
        if ($(this).val() !== '') {
            $('#submit-button').prop('disabled', false);
        } else {
            $('#submit-button').prop('disabled', true);
            return false;
        }
    });
}
/**
 * This function will check input field on changed
 * if and check all fields after that to make sure all required
 * fielsd are properly filled in
 */
$('#payment-form input[required]').change(function () {
    if ($(this).val() !== '') {
        $('#submit-button').prop('disabled', false);
        checkAllFields();
    } else {
        $('#submit-button').prop('disabled', true);
        return false;
    }
});