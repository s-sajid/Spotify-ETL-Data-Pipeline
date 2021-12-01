resource "aws_lambda_function" "spotify_analysis" {
    
    filename = "../payload.zip"
    function_name = "spotify_analysis"
    handler = "spotify_playlists.lambda_handler"

    role = "${aws_iam_role.lambda_execution_role.arn}"

    runtime = "python3.7"
    timeout = "120"

    environment {
        variables = {
            Spotify_Client_Id = var.Spotify_Client_ID,
            Spotify_Client_Secret = var.Spotify_Client_Secret
        }
    }
}