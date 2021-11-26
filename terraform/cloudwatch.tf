resource "aws_cloudwatch_event_rule" "weekly" {
    name = "weekly"
    description = "Triggers a cloudwatch event every week"
    schedule_expression = "rate(7 days)"
    is_enabled = false
}

resource "aws_cloudwatch_event_target" "trigger_cmo_strategy" {
  rule = "${aws_cloudwatch_event_rule.weekly.name}"
  target_id = "spotify_playlists"
  arn = "${aws_lambda_function.spotify_playlists.arn}"
}