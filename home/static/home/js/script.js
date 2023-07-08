var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});

// const options = {
//     mode: 'payment',
//     amount: 1099,
//     currency: 'usd',
//     // Fully customizable with appearance API.
//     appearance: {/*...*/},
//   };
  
//   // Set up Stripe.js and Elements to use in checkout form
//   const elements = stripe.elements(options);
  
//   // Create and mount the Payment Element
//   const paymentElement = elements.create('payment');
//   paymentElement.mount('#payment-element');

//   const form = document.getElementById('payment-form');
// const submitBtn = document.getElementById('submit');

// const handleError = (error) => {
//   const messageContainer = document.querySelector('#error-message');
//   messageContainer.textContent = error.message;
//   submitBtn.disabled = false;
// }

// form.addEventListener('submit', async (event) => {
//   // We don't want to let default form submission happen here,
//   // which would refresh the page.
//   event.preventDefault();

//   // Prevent multiple form submissions
//   if (submitBtn.disabled) {
//     return;
//   }

//   // Disable form submission while loading
//   submitBtn.disabled = true;

//   // Trigger form validation and wallet collection
//   const {error: submitError} = await elements.submit();
//   if (submitError) {
//     handleError(submitError);
//     return;
//   }

//   // Create the PaymentIntent and obtain clientSecret
//   const res = await fetch("/create-intent", {
//     method: "POST",
//   });

//   const {client_secret: clientSecret} = await res.json();

//   // Confirm the PaymentIntent using the details collected by the Payment Element
//   const {error} = await stripe.confirmPayment({
//     elements,
//     clientSecret,
//     confirmParams: {
//       return_url: 'https://8000-twilltp-project5ecommer-m4xg8d5e9zu.ws-eu101.gitpod.io/home/membership.html',
//     },
//   });

//   if (error) {
//     // This point is only reached if there's an immediate error when
//     // confirming the payment. Show the error to your customer (for example, payment details incomplete)
//     handleError(error);
//   } else {
//     // Your customer is redirected to your `return_url`. For some payment
//     // methods like iDEAL, your customer is redirected to an intermediate
//     // site first to authorize the payment, then redirected to the `return_url`.
//   }
// });