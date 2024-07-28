// @ts-check
import { initSchema } from '@aws-amplify/datastore';
import { schema } from './schema';



const { CryptoPrice } = initSchema(schema);

export {
  CryptoPrice
};