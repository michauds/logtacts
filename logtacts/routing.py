from channels.routing import route

channel_routing = {
    'send-invite': "invitations.consumers.send_invite",
    'process-stripe-webhook': "payments.consumers.process_webhook",
}