def cal_installment(amount, rate, year):
    installment = (amount + (amount * (rate / 100) * year)) / (year * 12)
    return installment
