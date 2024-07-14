URL="http://127.0.0.1:5000/api/timeline_post"

# Test if the post is created and save the id
CREATED_ID=$(curl -s -X POST "$URL" -d 'name=John&email=zrr.arshia@gmail.com&content=Test' | jq '.id')

echo "Created ID: $CREATED_ID"

# Print the full response to debug
RESPONSE=$(curl -s -X GET "$URL")

# Test if the post is created and the id is the same as the one saved
POST=$(echo "$RESPONSE" | jq --argjson id "$CREATED_ID" '.timeline_posts[] | select(.id == $id)')

if [ -z "$POST" ]; then
  echo "Test failed"
  exit 1
else
  echo "Saved successfully"
  # delete the post after the test
  DELETED_ID=$(curl -s -X DELETE "$URL/$CREATED_ID" | jq '.id')
  echo "Deleted ID: $DELETED_ID"
  exit 0
fi
