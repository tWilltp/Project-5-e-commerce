var stripe_publishable_key = $('#id_stripe_publishable_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var strpie = Stripe(stripe_publishable_key);
var elements = stripe.elements();
var card = elements.create('card');
card.mount('#card-element');