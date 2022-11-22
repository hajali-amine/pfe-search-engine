package loader

import (
	"context"
	"encoding/json"
	"os"
	"time"

	amqp "github.com/rabbitmq/amqp091-go"
)

func GetChannel() (*amqp.Connection, *amqp.Channel) {
	conn, err := amqp.Dial(os.Getenv("RABBITMQ_URL"))
	if err != nil {
		panic(err)
	}

	ch, err := conn.Channel()
	if err != nil {
		panic(err)
	}
	
	return conn, ch
}

// TODO: Test this with the scrapper
func PublishMsg(ch *amqp.Channel, msg interface{}) {
	q, err := ch.QueueDeclare(
		"loader", // name
		false,    // durable
		false,    // delete when unused
		false,    // exclusive
		false,    // no-wait
		nil,      // arguments
	)
	if err != nil {
		panic(err)
	}

	serializedMsg, err := json.Marshal(msg)
	if err != nil {
		panic(err)
	}

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	err = ch.PublishWithContext(ctx,
		"",     // exchange
		q.Name, // routing key
		false,  // mandatory
		false,  // immediate
		amqp.Publishing{
			ContentType: "application/json",
			Body:        []byte(serializedMsg),
		},
	)
	if err != nil {
		panic(err)
	}
}
