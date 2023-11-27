function request_payment(total) {
    let purchased = window.confirm("Your total is $" + total.toFixed(2) + ", do you wish to pay?");
    if (purchased) {
        return true;
    }
    else {
        return false;
    }
}