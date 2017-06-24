import Html exposing (Html, div)
import Time exposing (Time, millisecond)

-- Main
main: Program Never Model Msg
main =
  Html.program
    { init = init
    , view = view
    , update = update
    , subscriptions = subscriptions
    }


-- Models
type alias Model = Int

init: (Model, Cmd Msg)
init = ( 1, Cmd.none)


-- Updates
type Msg = Reset
  | Tick Time


update: Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    Reset ->
      init
    Tick newTime ->
      init


-- View

view: Model -> Html Msg
view model =
  div [] []

-- Subscriptions
subscriptions: Model -> Sub Msg
subscriptions model =
  Time.every (1000 / 24 * millisecond) Tick
