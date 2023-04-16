<?php

namespace App\Services;
use Junges\Kafka\Facades\Kafka;
use Junges\Kafka\Contracts\KafkaConsumerMessage;


class KafkaConsumer {

    function __construct() {

    }
    
    public function createConsumer($topic) {
        return Kafka::createConsumer()->subscribe($topic);
    }

    #configure supervisor to run process constantly in the background
    public function handleMessage($consumer) {
           $consumer
           ->withAutoCommit()
           ->withHandler(function(KafkaConsumeMessage $message) {

            $msgBody = $message->getBody();
            var_dump(json_decode($msgBody, true));

           })
           ->build();

           $consumer->consume();
    }
}