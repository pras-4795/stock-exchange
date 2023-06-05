## buy path
* greet
  - utter_greet
* buy{"stock_name":""}
  - utter_buy{"stock_name":""}
* goodbye
  - utter_goodbye
  - sample_custom_action

## sell path
* greet
  - utter_greet
* sell
  - utter_sell
* goodbye
  - utter_goodbye

## trending path
* greet
  - utter_greet
* trending
  - utter_top_5
* goodbye
  - utter_goodbye

## predict path
* greet
  - utter_greet
* predict
  - utter_positive_trend
* goodbye
  - utter_goodbye
