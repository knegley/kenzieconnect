import React from "react";
import Header from "./header";
import ReplyModal from "./replyModal";
import { StateContext } from "../App";
import { getInbox, toggleModal } from "./actions";
import { CardBody, Card, Row, CardText, Button } from "reactstrap";
import { getAuthData, getProfileData, handlePost } from "./helpers";
import { useHistory } from "react-router-dom";
const PenPal = (props) => {
  const { state, dispatch } = React.useContext(StateContext);
  const openModal = () => {
    dispatch(toggleModal());
  };
  const usersUrl = "http://127.0.0.1:8000/inbox/";
  let key = window.localStorage.getItem("key");
  const history = useHistory();

  React.useEffect(() => {
    const controller = new AbortController();
    const signal = controller.signal;
    if (history.action === "POP" || history.action === "PUSH") {
      (async () => {
        await getProfileData(key, dispatch, signal);
        await getAuthData(usersUrl, dispatch, getInbox, key);
      })();
    }
  }, [dispatch, key, history.action]);

  const handleSumbit = async (e) => {
    e.preventDefault();
    let form = e.target;
    const penpal_message = form.penpal_message.value;
    const to_user = form.to_user.value;
    const postData = { penpal_message, to_user };
    console.log(postData);
    await handlePost(postData);
    form.reset();
  };
  console.log(state.inbox);

  const messages =
    state.inbox &&
    state.inbox
      .filter((value) => !value.message_read)
      .map((value, index) => (
        <Card key={value.id} className="postcard">
          <CardBody className="postcardBody">
            <CardText>From:{value.from_user}</CardText>

            <CardText>{value.penpal_message}</CardText>
            <CardText>Recevied:{value.sent}</CardText>
            {/* This button needs to be wired up to bring up the replyModal 
          to send a message back to the user you are replying to */}
            <Button size="lg" onClick={() => openModal()}>
              Reply
            </Button>
            <ReplyModal
              show={state.modal}
              onHide={() => openModal()}
              index={index}
              email={value.from_email}
              id={value.id}
              penpal_message={value.penpal_message}
            />
          </CardBody>
        </Card>
      ));
  return (
    <React.Fragment>
      <div style={{ backgroundColor: "#4a5066" }}>
        <Header />
        <h1 className="penpalTitle">Messsages</h1>
        <form onSubmit={handleSumbit}>
          <input
            autoFocus
            placeholder="to: user@user.com"
            type="email"
            name="to_user"
          />
          <textarea
            id="message"
            name="penpal_message"
            cols="70"
            required={true}
            placeholder="enter message here"
            rows="3"
            maxLength="180"
          />
          <input type="submit" value="Send" />
        </form>
        <Row style={{ width: "60em", marginLeft: "10em" }}>{messages}</Row>
      </div>
    </React.Fragment>
  );
};

export default PenPal;
