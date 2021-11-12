resources "aws_lambda_function" "spotify_data_analysis" {
    
    filename = "../payload.zip"
    function_name = "spotify_data_analysis"
    handler = "spotify_playlists.lambda_handler"

    role = "${aws_iam_role.lambda_execution_role.arn}"

    runtime = "python3.7"
    timeout = "30"

    environment {
        variables = {
            Client_Id = var.TF_VAR_SPOTIPY_CLIENT_ID,
            Cleint_Secret = var.TF_VAR_SPOTIPY_CLIENT_SECRET
        }
    }
}