resource "aws_iam_role" "lambda_execution_role"{
    name = "lambda_execution_role"
    assume_role_policy = data.aws_iam_policy_document.lambda_trust_policy.json
}

resource "aws_iam_policy" "lambda_execution_policy" {
  name = "lambda_execution_policy"
  policy = data.aws_iam_policy_document.lambda_execution_policy_document.json
}