port module CharonGame exposing (..)
import Html exposing (Html, div)
import Time exposing (Time, millisecond)
import Keyboard exposing (KeyCode, downs)
import Char exposing (fromCode)
import String exposing (fromChar)
-- Look into Keyboard.Extra


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
type alias Model = (Int, Int)

type alias Delta = (Int, Int)

init: (Model, Cmd Msg)
init = ( (40, 13), render ((40, 13), "@"))


-- Updates
type Msg = Reset
  | Tick Time
  | KeyDown KeyCode


-- Left == 37 - Down == 40
deltaPosition: KeyCode -> (Int, Int)
deltaPosition code =
  case code of
    37 -> -- Left
      (-1, 0)
    38 -> -- Up
      (0, -1)
    39 -> -- Right
      (1, 0)
    40 -> -- Down
      (0, 1)
    _ ->
      (0, 0)


updatePosition: Model -> Delta -> Model
updatePosition model delta =
  let
    (nX, nY) = delta
    (x, y) = model
  in
    (x + nX, y + nY)

update: Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    Reset ->
      init
    Tick newTime ->
      (model, Cmd.none)
    KeyDown code ->
      let
        newPos = updatePosition model <| deltaPosition code
      in
        ( newPos, render (newPos, "@"))


-- View
view: Model -> Html Msg
view model =
  div [] []

-- Subscriptions
subscriptions: Model -> Sub Msg
subscriptions model =
  Sub.batch
    [ Time.every (1000 / 24 * millisecond) Tick
    , downs KeyDown
    ]


-- Ports
port render: (Model, String) -> Cmd msg
