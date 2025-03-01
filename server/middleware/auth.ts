import { CognitoJwtVerifier } from "aws-jwt-verify";

export default defineEventHandler(async (event) => {
  console.log('New request: ' + event.path)

  if(event.path.startsWith('/api/params'))
  {
    try
    {
      const verifier = CognitoJwtVerifier.create({
        userPoolId: process.env.UserPoolId ?? "",
        tokenUse: "id",
        clientId: process.env.ClientId ?? "",
      });

      const payload = await verifier.verify(getRequestHeader(event, 'Authorization')!);
      //console.log("Token is valid. Payload:", payload);
    }
    catch
    {
      //console.log("Token is invalid.")
      throw createError({ statusCode: 403, statusMessage: "Forbbiden, Not authenticated."});
    }
  }
})
