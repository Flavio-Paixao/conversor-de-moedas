

const amountInput = document.getElementById("amount");
const fromCurrency = document.getElementById("fromCurrency");
const toCurrency = document.getElementById("toCurrency");
const convertBtn = document.getElementById("convertBtn");
const resultDiv = document.getElementById("result");

const API_URL = "https://api.exchangerate.host/latest";

// 🔹 Preenche as opções de moedas dinamicamente
async function loadCurrencies() {

  const res = await fetch(API_URL);
  const data = await res.json();
  const currencies = Object.keys(data.rates);


  currencies.forEach(currency => {
    const option1 = document.createElement("option");
    option1.value = currency;
    option1.textContent = currency;

    const option2 = option1.cloneNode(true);

    fromCurrency.appendChild(option1);
    toCurrency.appendChild(option2);
  });

  // Define valores padrão
  fromCurrency.value = "BRL";
  toCurrency.value = "USD";
}

// 🔹 Faz a conversão consultando a API
async function convertCurrency() {
  const amount = parseFloat(amountInput.value);
  if (isNaN(amount) || amount <= 0) {
    resultDiv.textContent = "Por favor, insira um valor válido.";
    return;
  }

  const from = fromCurrency.value;
  const to = toCurrency.value;

  const res = await fetch(`${API_URL}?base=${from}&symbols=${to}`);
  const data = await res.json();

  const rate = data.rates[to];
  const converted = (amount * rate).toFixed(2);

  const resultText = `${amount.toFixed(2)} ${from} = ${converted} ${to}`;
  resultDiv.textContent = resultText;

  // Salva no localStorage
  localStorage.setItem("lastConversion", resultText);
}

// 🔹 Restaura última conversão
function restoreLastConversion() {
  const last = localStorage.getItem("lastConversion");
  if (last) {
    resultDiv.textContent = last;
  }
}

// Eventos
convertBtn.addEventListener("click", convertCurrency);

// Inicialização
loadCurrencies().then(restoreLastConversion);
