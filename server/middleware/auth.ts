import { CognitoJwtVerifier } from "aws-jwt-verify";


export default defineEventHandler(async (event) => {
  console.log('New request: ' + event.path)

//  console.log('secrets: ', getSecretEnv.provides)

  if(event.path.startsWith('/api/params'))
  {
    try
    {
      const verifier = CognitoJwtVerifier.create({
        userPoolId: "ap-northeast-1_N0bIGCilQ",
        tokenUse: "id",
        clientId: "5uvlhqe5n6rmnn8hv299h63nm2",
      });

      const payload = await verifier.verify(getRequestHeader(event, 'Authorization')!);
      //console.log("Token is valid. Payload:", payload);
    }
    catch
    {
      //console.log("Token is invalid.")
      //throw createError({ statusCode: 403, statusMessage: "Forbbiden, Not authenticated."});
    }
  }
})
