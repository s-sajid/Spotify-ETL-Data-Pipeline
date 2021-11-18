resources "aws_lambda_function" "spotify_data_analysis" {
    
    filename = "../payload.zip"
    function_name = "spotify_data_analysis"
    handler = "spotify_playlists.lambda_handler"

    role = "${aws_iam_role.lambda_execution_role.arn}"

    runtime = "python3.7"
    timeout = "30"

    environment {
        variables = {
            Client_Id = var.Spotify_Client_ID,
            Cleint_Secret = var.Spotify_Client_Secret
        }
    }
}