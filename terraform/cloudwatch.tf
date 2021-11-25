resource "aws_cloudwatch_event_rule" "weekly" {
    name = "weekly"
    description = "Triggers a cloudwatch event every week"
    schedule_expression = "rate(7 days)"
    is_enabled = false
}